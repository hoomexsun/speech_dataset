from typing import Callable, List, Tuple

from tqdm import tqdm
from correction import Correction
from steps.preprocessing import Preprocessing
from steps.res import Alphabet_resource, Correction_resource, Transliteration_resource
from transliteration import Transliteration
from steps.clusters import Clusters
from config.paths import *
from steps.utterance import Utterance
from utils.builder import MarkdownBuilderUtils
from utils.utils import Utils, Project


class DatasetProject(Project):
    def __init__(
        self, title: str = "main", num_files: int = 0, quiet: bool = True
    ) -> None:
        super().__init__(title, num_files, quiet)
        self.__init_res()
        self.__init_classes()
        self.__init_vars()

    def __init_classes(self, num_files: int = 0) -> None:
        self.set_num_files(num_files)
        self.p = Preprocessing(num_files=num_files)
        self.u = Utterance(num_files=num_files)
        self.c = Correction(num_files=num_files)
        self.t = Transliteration(num_files=num_files)

    def __init_vars(self):
        self.s550_utts = dict()
        self.bn_utts = dict()
        self.mm_utts = dict()

    def __init_res(self):
        cr = Correction_resource()
        tr = Transliteration_resource()
        ar = Alphabet_resource()

    # ! This will overwrite existing files, take care!!!
    # @staticmethod
    # def build_raw_dir():
    #     files = Utils.get_files(dir=RTF_DATA, extension="rtf")
    #     for file_path in files:
    #         Utils.write_text_file(
    #             content="",
    #             file_path=self.build_path(file_path=file_path, dir=RAW_DATA),
    #             exist_ok=False,
    #         )

    # TODO: Restructure progress bar using tqdm DONE
    # TODO: Move every basic steps to LOG style formatting
    # TODO: Divide the different major steps into different functions. Use self for shared variable.
    def run(self, rtf: bool = False):
        if rtf:
            files = Utils.get_files(dir=RTF_DATA, extension="rtf")
        else:
            files = Utils.get_files(dir=RAW_DATA)

        self.__init_classes(len(files))

        # Step 0: Preprocessing [NEW]
        self.from_dir(
            dir=RAW_DATA,
            desc="Preprocessing Files",
            func=self.p.preprocess_file,
            output_dir=SCP_S550_DIR,
        )

        # Step 1: Utterances [NEW]
        self.s550_utts = self.from_dir(
            dir=SCP_S550_DIR,
            desc="Building Utterances",
            func=self.u.utterance,
            output_dir=UTT_S550_DIR,
            content_as_dict=True,
        )

        # Step 1.1: Write s550 text
        self.display(
            title=self.u.title, target=TEXT_S550_FILE.as_posix(), desc="saving"
        )
        Utils.write_text_file(
            content=self.u.utt_dict_to_content(self.s550_utts), file_path=TEXT_S550_FILE
        )

        # prep
        utterances = self.u.get_utterances_from_text(file_path=TEXT_S550_FILE)
        # Step 1.2: Write s550 words
        self.save_words(content=utterances, file_path=WORDS_S550_FILE)
        # Step 1.3: Write s550 chars
        self.save_chars(content=utterances, file_path=CHARS_S550_FILE, avoid_utf=False)

        # Step 2: Correction
        # Step 2.0.1: Correction of Scripts
        # Step 2.0.1: Correction of Scripts [NEW]
        self.from_dir(
            dir=SCP_S550_DIR,
            desc="Correcting Scripts",
            func=self.c.correct_script,
            output_dir=SCP_BN_DIR,
        )

        # Step 2.0.2: Correction of Utterances [NEW]
        self.bn_utts = self.from_dir(
            dir=UTT_S550_DIR,
            desc="Correcting Utterances",
            func=self.c.correct_utterances,
            output_dir=UTT_BN_DIR,
            content_as_dict=True,
        )

        # Step 2.1: Write bn text
        self.display(title=self.u.title, target=TEXT_BN_FILE.as_posix(), desc="saving")
        Utils.write_text_file(
            content=self.u.utt_dict_to_content(self.bn_utts), file_path=TEXT_BN_FILE
        )

        # Prep
        utterances = self.u.get_utterances_from_text(file_path=TEXT_BN_FILE)
        # Step 2.2: Write bn words
        self.save_words(content=utterances, file_path=WORDS_BN_FILE)
        # Step 2.3: Write bn chars
        self.save_chars(content=utterances, file_path=CHARS_BN_FILE, avoid_utf=False)

        # Step 3: Transliteration
        # Step 3.0.1: Transliteration of Scripts [NEW]
        self.from_dir(
            dir=SCP_BN_DIR,
            desc="Transliterating Scripts",
            func=self.t.transliterate_script,
            output_dir=SCP_MM_DIR,
        )

        # Step 3.0.2: Transliteration of Utterances [NEW]
        self.mm_utts = self.from_dir(
            dir=UTT_BN_DIR,
            desc="Transliterating Utterances",
            func=self.t.transliterate_utterances,
            output_dir=UTT_MM_DIR,
            content_as_dict=True,
        )

        # Step 3.1: Write mm text
        Utils.display_line(
            title=self.u.title, target=TEXT_MM_FILE.as_posix(), suffix="saving"
        )
        Utils.write_text_file(
            content=self.u.utt_dict_to_content(self.mm_utts), file_path=TEXT_MM_FILE
        )

        # Prep
        utterances = self.u.get_utterances_from_text(file_path=TEXT_MM_FILE)
        # Step 3.2: Write mm words
        self.save_words(content=utterances, file_path=WORDS_MM_FILE)
        # Step 3.3: Write mm chars
        self.save_chars(content=utterances, file_path=CHARS_MM_FILE, avoid_utf=False)

        # Step 4: Extra
        # Step 4.1: Generate WordMap
        # Step 4.1.1: Generate S550_BN WordMap
        self.generate_wordmap(
            file_path=WORDS_S550_FILE, fun=self.c.correct, lang1=S550, lang2=BN
        )
        # Step 4.1.2: Generate BN_MM WordMap
        self.generate_wordmap(
            file_path=WORDS_BN_FILE, fun=self.t.transliterate, lang1=BN, lang2=MM
        )
        # Step 4.2 Generate Clusters Info
        bn_words = Utils.read_encoded_file(file_path=WORDS_BN_FILE).split("\n")
        self.generate_clusters_info(bn_words=bn_words)

    # Run files
    def from_dir(
        self,
        dir: Path,
        desc: str,
        func: Callable,
        output_dir: Path,
        content_as_dict: bool = False,
    ):
        content_dict = {}
        files = Utils.get_files(dir=dir, extension="txt")
        for idx, file_path in enumerate(tqdm(files, total=len(files), desc=desc)):
            content = func(file_path=file_path)
            Utils.write_text_file(
                content=content,
                file_path=Project.change_path(file_path=file_path, dir=output_dir),
            )
            if content_as_dict:
                content_dict.update(self.u.utt_content_to_dict(content))
        return content_dict

    @staticmethod
    def save_words(content: str, file_path: Path, avoid_utf: bool = True) -> None:
        words = "\n".join(sorted(set(content.split())))
        Utils.display_line(
            title="Words", target=file_path.as_posix(), suffix="saving words file"
        )
        Utils.write_text_file(content=words, file_path=file_path)
        if not avoid_utf:
            Utils.write_text_file(content=words, file_path=file_path, unicode=True)

    @staticmethod
    def save_chars(content: str, file_path: Path, avoid_utf: bool = True) -> None:
        chars = "\n".join(sorted(set(content)))
        Utils.display_line(
            title="Characters",
            target=file_path.as_posix(),
            suffix="saving characters file",
        )
        Utils.write_text_file(content=chars, file_path=file_path)
        if not avoid_utf:
            Utils.write_text_file(
                content=chars, file_path=file_path, unicode=True, skip_newline=True
            )

    @staticmethod
    def generate_wordmap(file_path: Path, fun, lang1: str, lang2: str):
        content = Utils.read_encoded_file(file_path)
        wmap = {word: fun(word) for word in content.split("\n")}
        output_filename = f"{lang1}_{lang2}"
        Utils.write_json_file(data=wmap, file_path=WORD_MAP_DIR / output_filename)
        Utils.write_csv_file(
            data=wmap,
            fieldnames=(lang1, lang2),
            file_path=WORD_MAP_DIR / output_filename,
        )

    @staticmethod
    def generate_clusters_info(bn_words: List[str]):
        # Step 4.2.1: Build clusters
        clusters = Clusters.get_clusters(content="\n".join(bn_words))
        clusters = sorted(clusters)
        Utils.display_line(
            title="clusters",
            target=CLUSTERS_FILE.as_posix(),
            suffix="writing-clusters-file",
        )
        Utils.write_text_file(content="\n".join(clusters), file_path=CLUSTERS_FILE)  # type: ignore

        # Step 4.2.2: Build clusters with examples
        clusters_egs = Clusters.build_egs(
            content="\n".join(bn_words), clusters=clusters
        )
        Utils.display_line(
            title="clusters",
            target=CLUSTERS_EGS_FILE.as_posix(),
            suffix="writing-clusters-examples-file",
        )
        Utils.write_json_file(data=clusters_egs, file_path=CLUSTERS_EGS_FILE)
        Utils.write_json_file(
            data=clusters_egs, file_path=CLUSTERS_EGS_FILE, unicode=True
        )

        MarkdownBuilderUtils.build_markdown_file(
            d=clusters_egs, file_name=CLUSTERS_EGS_FILE.stem  # type: ignore
        )

        # Step 4.2.3: Build clusters map
        clusters_map = Clusters.build_probable_map(clusters=clusters)
        Utils.display_line(
            title="clusters",
            target=CLUSTERS_MAP_FILE.as_posix(),
            suffix="writing-clusters-map-file",
        )
        Utils.write_json_file(data=clusters_map, file_path=CLUSTERS_MAP_FILE)
        Utils.write_json_file(
            data=clusters_map, file_path=CLUSTERS_MAP_FILE, unicode=True
        )
        MarkdownBuilderUtils.build_markdown_file(
            d=clusters_map, file_name=CLUSTERS_MAP_FILE.stem  # type: ignore
        )

        # Step 4.2.4: Build detailed cluster dictionary
        clusters_detailed, clusters_pct = Clusters.build_detailed_clusters(
            cluster_egs=clusters_egs, total_words=len(bn_words)
        )
        Utils.display_line(
            title="clusters",
            target=CLUSTERS_DETAILED_FILE.as_posix(),
            suffix="writing-clusters-detailed-file",
        )
        Utils.write_json_file(data=clusters_detailed, file_path=CLUSTERS_DETAILED_FILE)
        Utils.write_json_file(
            data=clusters_detailed,
            file_path=CLUSTERS_DETAILED_FILE,
            unicode=True,
        )
        Utils.write_json_file(data=clusters_pct, file_path=CLUSTERS_PCT_FILE)
        Utils.write_json_file(
            data=clusters_pct, file_path=CLUSTERS_PCT_FILE, unicode=True
        )
        MarkdownBuilderUtils.build_markdown_file(
            d=clusters_pct, file_name=CLUSTERS_PCT_FILE.stem
        )
