from pathlib import Path
from typing import Callable, Dict, List

from tqdm import tqdm
from config.paths import (
    BN,
    CHARS_BN_FILE,
    CHARS_MM_FILE,
    CHARS_S550_FILE,
    CLUSTERS_DETAILED_FILE,
    CLUSTERS_EGS_FILE,
    CLUSTERS_FILE,
    CLUSTERS_MAP_FILE,
    CLUSTERS_PCT_FILE,
    MM,
    RAW_DATA,
    RTF_DATA,
    S550,
    SCP_BN_DIR,
    SCP_MM_DIR,
    SCP_S550_DIR,
    TEXT_BN_FILE,
    TEXT_MM_FILE,
    TEXT_S550_FILE,
    UTT_BN_DIR,
    UTT_MM_DIR,
    UTT_S550_DIR,
    WORD_MAP_DIR,
    WORDS_BN_FILE,
    WORDS_MM_FILE,
    WORDS_S550_FILE,
)
from config.project import Project
from correction import Correction
from steps.preprocessing import Preprocessing
from steps.res import init_resources
from transliteration import Transliteration
from steps.clusters import Clusters
from steps.utterance import Utterance
from utils.builder import MarkdownBuilderUtils
from utils.display import display_line
from utils.file import (
    change_path,
    get_files,
    get_utterances_from_text,
    read_encoded_file,
    write_csv_file,
    write_json_file,
    write_text_file,
)
from utils.text import utt_content_to_dict, utt_dict_to_content


class DatasetProject(Project):
    def __init__(self) -> None:
        super().__init__("main")
        init_resources()
        self.__init_classes()
        self.__init_vars()

    def __init_classes(self, num_files: int = 0) -> None:
        self.p = Preprocessing()
        self.u = Utterance()
        self.c = Correction()
        self.t = Transliteration()

    def __init_vars(self):
        self.s550_utts = dict()
        self.bn_utts = dict()
        self.mm_utts = dict()

    # TODO: Restructure progress bar using tqdm DONE
    # TODO: Move every basic steps to LOG style formatting
    # TODO: Divide the different major steps into different functions. Use self for shared variable.
    def run(self, rtf: bool = False):
        if rtf:
            files = get_files(dir=RTF_DATA, extension="rtf")
        else:
            files = get_files(dir=RAW_DATA)

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
        display_line(
            title=self.u.title,
            target=TEXT_S550_FILE.as_posix(),
            desc="saving utterance file",
        )
        write_text_file(
            content=utt_dict_to_content(self.s550_utts), file_path=TEXT_S550_FILE
        )

        # prep
        utterances = get_utterances_from_text(file_path=TEXT_S550_FILE)
        # Step 1.2: Write s550 words
        self.save_words_file(content=utterances, file_path=WORDS_S550_FILE)
        # Step 1.3: Write s550 chars
        self.save_chars_file(
            content=utterances, file_path=CHARS_S550_FILE, avoid_utf=False
        )

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
        self.save_utterance_file(utt_dict=self.bn_utts, file_path=TEXT_BN_FILE)

        # Prep
        utterances = get_utterances_from_text(file_path=TEXT_BN_FILE)
        # Step 2.2: Write bn words
        self.save_words_file(content=utterances, file_path=WORDS_BN_FILE)
        # Step 2.3: Write bn chars
        self.save_chars_file(
            content=utterances, file_path=CHARS_BN_FILE, avoid_utf=False
        )

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
        self.save_utterance_file(utt_dict=self.mm_utts, file_path=TEXT_MM_FILE)

        # Prep
        utterances = get_utterances_from_text(file_path=TEXT_MM_FILE)
        # Step 3.2: Write mm words
        self.save_words_file(content=utterances, file_path=WORDS_MM_FILE)
        # Step 3.3: Write mm chars
        self.save_chars_file(
            content=utterances, file_path=CHARS_MM_FILE, avoid_utf=False
        )

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
        bn_words = read_encoded_file(file_path=WORDS_BN_FILE).split("\n")
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
        files = get_files(dir=dir, extension="txt")
        for file_path in tqdm(files, total=len(files), desc=desc):
            content = func(file_path=file_path)
            write_text_file(
                content=content,
                file_path=change_path(file_path=file_path, dir=output_dir),
            )
            if content_as_dict:
                content_dict.update(utt_content_to_dict(content))
        return content_dict

    @staticmethod
    def save_utterance_file(utt_dict: Dict, file_path: Path) -> None:
        display_line(
            title="Utterance",
            target=file_path.as_posix(),
            desc="saving utterance file",
        )
        write_text_file(content=utt_dict_to_content(utt_dict), file_path=file_path)

    @staticmethod
    def save_words_file(content: str, file_path: Path, avoid_utf: bool = True) -> None:
        words = "\n".join(sorted(set(content.split())))
        display_line(
            title="Words", target=file_path.as_posix(), desc="saving words file"
        )
        write_text_file(content=words, file_path=file_path)
        if not avoid_utf:
            write_text_file(content=words, file_path=file_path, unicode=True)

    @staticmethod
    def save_chars_file(content: str, file_path: Path, avoid_utf: bool = True) -> None:
        chars = "\n".join(sorted(set(content)))
        display_line(
            title="Characters",
            target=file_path.as_posix(),
            desc="saving characters file",
        )
        write_text_file(content=chars, file_path=file_path)
        if not avoid_utf:
            write_text_file(
                content=chars, file_path=file_path, unicode=True, skip_newline=True
            )

    @staticmethod
    def generate_wordmap(file_path: Path, fun, lang1: str, lang2: str):
        content = read_encoded_file(file_path)
        wmap = {word: fun(word) for word in content.split("\n")}
        output_filename = f"{lang1}_{lang2}"
        write_json_file(data=wmap, file_path=WORD_MAP_DIR / output_filename)
        write_csv_file(
            data=wmap,
            fieldnames=(lang1, lang2),
            file_path=WORD_MAP_DIR / output_filename,
        )

    @staticmethod
    def generate_clusters_info(bn_words: List[str]):
        # Step 4.2.1: Build clusters
        clusters = Clusters.get_clusters(content="\n".join(bn_words))
        clusters = sorted(clusters)
        display_line(
            title="clusters",
            target=CLUSTERS_FILE.as_posix(),
            desc="writing-clusters-file",
        )
        write_text_file(content="\n".join(clusters), file_path=CLUSTERS_FILE)  # type: ignore

        # Step 4.2.2: Build clusters with examples
        clusters_egs = Clusters.build_egs(
            content="\n".join(bn_words), clusters=clusters
        )
        display_line(
            title="clusters",
            target=CLUSTERS_EGS_FILE.as_posix(),
            desc="writing-clusters-examples-file",
        )
        write_json_file(data=clusters_egs, file_path=CLUSTERS_EGS_FILE)
        write_json_file(data=clusters_egs, file_path=CLUSTERS_EGS_FILE, unicode=True)

        MarkdownBuilderUtils.build_markdown_file(
            d=clusters_egs, file_name=CLUSTERS_EGS_FILE.stem  # type: ignore
        )

        # Step 4.2.3: Build clusters map
        clusters_map = Clusters.build_probable_map(clusters=clusters)
        display_line(
            title="clusters",
            target=CLUSTERS_MAP_FILE.as_posix(),
            desc="writing-clusters-map-file",
        )
        write_json_file(data=clusters_map, file_path=CLUSTERS_MAP_FILE)
        write_json_file(data=clusters_map, file_path=CLUSTERS_MAP_FILE, unicode=True)
        MarkdownBuilderUtils.build_markdown_file(
            d=clusters_map, file_name=CLUSTERS_MAP_FILE.stem  # type: ignore
        )

        # Step 4.2.4: Build detailed cluster dictionary
        clusters_detailed, clusters_pct = Clusters.build_detailed_clusters(
            cluster_egs=clusters_egs, total_words=len(bn_words)
        )
        display_line(
            title="clusters",
            target=CLUSTERS_DETAILED_FILE.as_posix(),
            desc="writing-clusters-detailed-file",
        )
        write_json_file(data=clusters_detailed, file_path=CLUSTERS_DETAILED_FILE)
        write_json_file(
            data=clusters_detailed,
            file_path=CLUSTERS_DETAILED_FILE,
            unicode=True,
        )
        write_json_file(data=clusters_pct, file_path=CLUSTERS_PCT_FILE)
        write_json_file(data=clusters_pct, file_path=CLUSTERS_PCT_FILE, unicode=True)
        MarkdownBuilderUtils.build_markdown_file(
            d=clusters_pct, file_name=CLUSTERS_PCT_FILE.stem
        )
