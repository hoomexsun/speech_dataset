from pathlib import Path
from typing import Dict, List
from src.config.constants import Language
from src.config.paths import (
    CHARS_BN_FILE,
    CHARS_MM_FILE,
    CHARS_S550_FILE,
    CLUSTERS_DETAILED_FILE,
    CLUSTERS_EGS_FILE,
    CLUSTERS_FILE,
    CLUSTERS_MAP_FILE,
    CLUSTERS_PCT_FILE,
    RAW_DATA,
    NEWS_BN_DIR,
    NEWS_MM_DIR,
    NEWS_S550_DIR,
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
from src.utils.project import Project, process_directory
from src.core.correction import Correction
from src.core.preprocessing import Preprocessing
from src.core.res import init_resources
from src.core.clusterization import Clusters
from src.core.utterance import Utterance
from src.core.transliteration import Transliteration
from src.utils.display import display_line
from src.utils.file import fread, fwrite_csv, fwrite_json, fwrite_text, fget_utterances
from src.utils.text import utt_dict_to_content
from src.utils.builder import MarkdownBuilderUtils


class DatasetProject(Project):
    def __init__(self) -> None:
        super().__init__("main")
        init_resources()
        self.__init_classes()
        self.__init_vars()

    def __init_classes(self) -> None:
        self.p = Preprocessing()
        self.u = Utterance()
        self.c = Correction()
        self.t = Transliteration()

    def __init_vars(self):
        self.s550_utts = dict()
        self.bn_utts = dict()
        self.mm_utts = dict()

    def run(self):
        # Step 0: Preprocessing [NEW]
        process_directory(
            func=self.p.preprocess_file,
            dir=RAW_DATA,
            output_dir=NEWS_S550_DIR,
            desc="Preprocessing Files",
        )

        # Step 1: Utterances [NEW]
        self.s550_utts = process_directory(
            func=self.u.utterance,
            dir=NEWS_S550_DIR,
            output_dir=UTT_S550_DIR,
            desc="Building Utterances",
            return_dict=True,
        )

        # Step 1.1: Write s550 text
        display_line(
            title=self.u.title,
            target=TEXT_S550_FILE.as_posix(),
            desc="saving utterance file",
        )
        fwrite_text(
            content=utt_dict_to_content(self.s550_utts), file_path=TEXT_S550_FILE
        )

        # Step 1.2: Write s550 words
        self.save_words_file(utt_path=TEXT_S550_FILE, file_path=WORDS_S550_FILE)
        # Step 1.3: Write s550 chars
        self.save_chars_file(
            utt_path=TEXT_S550_FILE, file_path=CHARS_S550_FILE, utf=True
        )

        # Step 2: Correction
        # Step 2.0.1: Correction of Scripts
        # Step 2.0.1: Correction of Scripts [NEW]
        process_directory(
            func=self.c.correct_script,
            dir=NEWS_S550_DIR,
            output_dir=NEWS_BN_DIR,
            desc="Correcting News",
        )

        # Step 2.0.2: Correction of Utterances [NEW]
        self.bn_utts = process_directory(
            func=self.c.correct_utterances,
            dir=UTT_S550_DIR,
            output_dir=UTT_BN_DIR,
            desc="Correcting Utterances",
            return_dict=True,
        )

        # Step 2.1: Write bn text
        self.save_utterance_file(utt_dict=self.bn_utts, file_path=TEXT_BN_FILE)

        # Step 2.2: Write bn words
        self.save_words_file(utt_path=TEXT_BN_FILE, file_path=WORDS_BN_FILE)
        # Step 2.3: Write bn chars
        self.save_chars_file(utt_path=TEXT_BN_FILE, file_path=CHARS_BN_FILE, utf=True)

        # Step 3: Transliteration
        # Step 3.0.1: Transliteration of Scripts [NEW]
        process_directory(
            func=self.t.transliterate_script,
            dir=NEWS_BN_DIR,
            output_dir=NEWS_MM_DIR,
            desc="Transliterating News",
        )

        # Step 3.0.2: Transliteration of Utterances [NEW]
        self.mm_utts = process_directory(
            func=self.t.transliterate_utterances,
            desc="Transliterating Utterances",
            dir=UTT_BN_DIR,
            output_dir=UTT_MM_DIR,
            return_dict=True,
        )

        # Step 3.1: Write mm text
        self.save_utterance_file(utt_dict=self.mm_utts, file_path=TEXT_MM_FILE)
        # Step 3.2: Write mm words
        self.save_words_file(utt_path=TEXT_MM_FILE, file_path=WORDS_MM_FILE)
        # Step 3.3: Write mm chars
        self.save_chars_file(utt_path=TEXT_MM_FILE, file_path=CHARS_MM_FILE, utf=True)

        # Step 4: Extra
        # Step 4.1: Generate WordMap
        # Step 4.1.1: Generate S550_BN WordMap
        self.generate_wordmap(
            file_path=WORDS_S550_FILE,
            fun=self.c.correct,
            lang1=Language.S550.value,
            lang2=Language.BN.value,
        )
        # Step 4.1.2: Generate BN_MM WordMap
        self.generate_wordmap(
            file_path=WORDS_BN_FILE,
            fun=self.t.transliterate,
            lang1=Language.BN.value,
            lang2=Language.MM.value,
        )
        # Step 4.2 Generate Clusters Info
        bn_words = fread(file_path=WORDS_BN_FILE).split("\n")
        self.generate_clusters_info(bn_words=bn_words)

    @staticmethod
    def save_utterance_file(utt_dict: Dict, file_path: Path) -> None:
        display_line(
            title="Utterance",
            target=file_path.as_posix(),
            desc="saving utterance file",
        )
        fwrite_text(content=utt_dict_to_content(utt_dict), file_path=file_path)

    @staticmethod
    def save_words_file(
        utt_path: Path, file_path: Path, avoid_utf: bool = True
    ) -> None:
        content = fget_utterances(file_path=utt_path)
        words = "\n".join(sorted(set(content.split())))
        display_line(
            title="Words", target=file_path.as_posix(), desc="saving words file"
        )
        fwrite_text(content=words, file_path=file_path)
        if not avoid_utf:
            fwrite_text(content=words, file_path=file_path, unicode=True)

    @staticmethod
    def save_chars_file(utt_path: Path, file_path: Path, utf: bool = False) -> None:
        content = fget_utterances(file_path=utt_path)
        chars = "\n".join(sorted(set(content)))
        display_line(
            title="Characters",
            target=file_path.as_posix(),
            desc="saving characters file",
        )
        fwrite_text(content=chars, file_path=file_path)
        if utf:
            fwrite_text(
                content=chars, file_path=file_path, unicode=True, skip_newline=True
            )

    @staticmethod
    def generate_wordmap(file_path: Path, fun, lang1: str, lang2: str):
        content = fread(file_path)
        wmap = {word: fun(word) for word in content.split("\n")}
        output_filename = f"{lang1}_{lang2}"
        fwrite_json(data=wmap, file_path=WORD_MAP_DIR / output_filename)
        fwrite_csv(
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
        fwrite_text(content="\n".join(clusters), file_path=CLUSTERS_FILE)  # type: ignore

        # Step 4.2.2: Build clusters with examples
        clusters_egs = Clusters.build_egs(
            content="\n".join(bn_words), clusters=clusters
        )
        display_line(
            title="clusters",
            target=CLUSTERS_EGS_FILE.as_posix(),
            desc="writing-clusters-examples-file",
        )
        fwrite_json(data=clusters_egs, file_path=CLUSTERS_EGS_FILE)
        fwrite_json(data=clusters_egs, file_path=CLUSTERS_EGS_FILE, unicode=True)

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
        fwrite_json(data=clusters_map, file_path=CLUSTERS_MAP_FILE)
        fwrite_json(data=clusters_map, file_path=CLUSTERS_MAP_FILE, unicode=True)
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
        fwrite_json(data=clusters_detailed, file_path=CLUSTERS_DETAILED_FILE)
        fwrite_json(
            data=clusters_detailed,
            file_path=CLUSTERS_DETAILED_FILE,
            unicode=True,
        )
        fwrite_json(data=clusters_pct, file_path=CLUSTERS_PCT_FILE)
        fwrite_json(data=clusters_pct, file_path=CLUSTERS_PCT_FILE, unicode=True)
        MarkdownBuilderUtils.build_markdown_file(
            d=clusters_pct, file_name=CLUSTERS_PCT_FILE.stem
        )
