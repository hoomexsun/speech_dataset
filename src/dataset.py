from pathlib import Path
from typing import Callable, Dict
from config import (
    CHARS_BN_FILE,
    CHARS_S550_FILE,
    RAW_DATA,
    NEWS_BN_DIR,
    NEWS_S550_DIR,
    TEXT_BN_FILE,
    TEXT_S550_FILE,
    UTT_BN_DIR,
    UTT_S550_DIR,
    WORD_MAP_DIR,
    WORDS_BN_FILE,
    WORDS_S550_FILE,
    Language,
)
from .modules.glyph_correction import GlyphCorrection
from .modules.mm_transliteration import MMTransliteration
from .preprocessing import Preprocessing
from .segmentation import Segmentation
from .utils.file import (
    process_directory,
    read_file,
    read_utterances,
    write_csv,
    write_json,
    write_text,
)
from .utils.utterance import dict_to_str


class DatasetProject:
    def __init__(self) -> None:
        super().__init__()
        self.p = Preprocessing()
        self.s = Segmentation()
        self.gc = GlyphCorrection()
        self.mt = MMTransliteration()
        self.s550_utts = dict()
        self.bn_utts = dict()
        self.mm_utts = dict()

    def run(self):
        # Step 0: Preprocessing
        process_directory(
            fn=self.p.preprocess_file,
            input_dir=RAW_DATA,
            output_dir=NEWS_S550_DIR,
            desc="Preprocessing Files",
        )

        # Step 1: Utterances
        self.s550_utts = process_directory(
            fn=self.s.segment,
            input_dir=NEWS_S550_DIR,
            output_dir=UTT_S550_DIR,
            desc="Building Utterances",
            return_result=True,
        )

        # Step 1.1: Write s550 text
        print(f"[{str(self.s)}] saving utterance file at {TEXT_S550_FILE.as_posix()}")
        write_text(content=dict_to_str(self.s550_utts), dest=TEXT_S550_FILE)

        # Step 1.2: Write s550 words
        self.save_words_file(utt_path=TEXT_S550_FILE, dest=WORDS_S550_FILE)
        # Step 1.3: Write s550 chars
        self.save_chars_file(utt_path=TEXT_S550_FILE, dest=CHARS_S550_FILE, utf=True)

        # Step 2: Correction
        # Step 2.0.1: Correction of Scripts
        process_directory(
            fn=self.gc.correct_script,
            input_dir=NEWS_S550_DIR,
            output_dir=NEWS_BN_DIR,
            desc="Correcting News",
        )

        # Step 2.0.2: Correction of Utterances
        self.bn_utts = process_directory(
            fn=self.gc.correct_utterances,
            input_dir=UTT_S550_DIR,
            output_dir=UTT_BN_DIR,
            desc="Correcting Utterances",
            return_result=True,
        )

        # Step 2.1: Write bn text
        self.save_utterance_file(utt_dict=self.bn_utts, dest=TEXT_BN_FILE)
        # Step 2.2: Write bn words
        self.save_words_file(utt_path=TEXT_BN_FILE, dest=WORDS_BN_FILE)
        # Step 2.3: Write bn chars
        self.save_chars_file(utt_path=TEXT_BN_FILE, dest=CHARS_BN_FILE, utf=True)

        # # Step 3: Transliteration
        # # Step 3.0.1: Transliteration of Scripts
        # process_directory(
        #     fn=self.t.transliterate_script,
        #     input_dir=NEWS_BN_DIR,
        #     output_dir=NEWS_MM_DIR,
        #     desc="Transliterating News",
        # )

        # # Step 3.0.2: Transliteration of Utterances
        # self.mm_utts = process_directory(
        #     fn=self.t.transliterate_utterances,
        #     input_dir=UTT_BN_DIR,
        #     output_dir=UTT_MM_DIR,
        #     desc="Transliterating Utterances",
        #     return_result=True,
        # )

        # # Step 3.1: Write mm text
        # self.save_utterance_file(utt_dict=self.mm_utts, dest=TEXT_MM_FILE)
        # # Step 3.2: Write mm words
        # self.save_words_file(utt_path=TEXT_MM_FILE, dest=WORDS_MM_FILE)
        # # Step 3.3: Write mm chars
        # self.save_chars_file(utt_path=TEXT_MM_FILE, dest=CHARS_MM_FILE, utf=True)

        # # Step 4: Extra
        # # Step 4.1: Generate WordMap
        # # Step 4.1.1: Generate S550_BN WordMap
        self.generate_wordmap(
            dest=WORDS_S550_FILE,
            fn=self.gc.correct,
            lang1=Language.S550.value,
            lang2=Language.BN.value,
        )
        # # Step 4.1.2: Generate BN_MM WordMap
        # self.generate_wordmap(
        #     file_path=WORDS_BN_FILE,
        #     fun=self.t.transliterate,
        #     lang1=Language.BN.value,
        #     lang2=Language.MM.value,
        # )
        # # Step 4.2 Generate Clusters Info
        # bn_words = read_file(file_path=WORDS_BN_FILE).split("\n")
        # self.generate_clusters_info(bn_words=bn_words)

    @staticmethod
    def save_utterance_file(utt_dict: Dict, dest: Path) -> None:
        print(f"[Utterance] saving utterance file at {dest.as_posix()}")
        write_text(content=dict_to_str(utt_dict), dest=dest)

    @staticmethod
    def save_words_file(utt_path: Path, dest: Path, avoid_utf: bool = True) -> None:
        content = read_utterances(file_path=utt_path)
        words = "\n".join(sorted(set(content.split())))
        print(f"[Words] saving words file at {dest.as_posix()}")
        write_text(content=words, dest=dest)
        if not avoid_utf:
            write_text(content=words, dest=dest, use_unicode=True)

    @staticmethod
    def save_chars_file(utt_path: Path, dest: Path, utf: bool = False) -> None:
        chars = "\n".join(sorted(set(read_utterances(utt_path))))
        print(f"[Characters] saving characters file at {TEXT_S550_FILE.as_posix()}")
        write_text(content=chars, dest=dest)
        if utf:
            write_text(content=chars, dest=dest, use_unicode=True, skip_newline=True)

    @staticmethod
    def generate_wordmap(dest: Path, fn: Callable, lang1: str, lang2: str):
        content = read_file(dest)
        wmap = {word: fn(word) for word in content.split("\n")}
        output_filename = f"{lang1}_{lang2}"

        print(
            f"[Wordmap] saving wordmap file at {Path(WORD_MAP_DIR / output_filename).as_posix()}"
        )
        write_text(
            content="\n".join(
                [f"{word}\t{corrected}" for word, corrected in wmap.items()]
            ),
            dest=WORD_MAP_DIR / output_filename,
        )
        write_json(data=wmap, dest=WORD_MAP_DIR / output_filename)
        write_csv(
            data=wmap,
            fieldnames=(lang1, lang2),
            dest=WORD_MAP_DIR / output_filename,
        )
