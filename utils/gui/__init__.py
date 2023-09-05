from tkinter import Misc, ttk
import tkinter as tk
from typing import Callable, List, Tuple
from config.constants import Language
from config.paths import (
    CHARS_BN_FILE,
    CHARS_MM_FILE,
    CHARS_S550_FILE,
    WORDS_BN_FILE,
    WORDS_MM_FILE,
    WORDS_S550_FILE,
)
from correction import Correction
from transliteration import Transliteration

from utils.file import fget_list
from .test_frame import TestFrame
from .analyze_frame import AnalyzeFrame


__all__ = [
    "MainFrame",
    "TestFrame",
    "AnalyzeFrame",
]


class MainFrame(ttk.Notebook):
    def __init__(
        self,
        master: Misc | None = None,
    ) -> None:
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)
        self.load_content()
        self.load_frames()

    def load_content(self):
        self.s550_words = fget_list(WORDS_S550_FILE)
        self.bn_words = fget_list(WORDS_BN_FILE)
        self.mm_words = fget_list(WORDS_MM_FILE)
        self.s550_chars = fget_list(CHARS_S550_FILE)
        self.bn_chars = fget_list(CHARS_BN_FILE)
        self.mm_chars = fget_list(CHARS_MM_FILE)

    def reload_content(self, lang: Language) -> Tuple[List[str], List[str]]:
        if lang == Language.S550:
            return self.s550_words, self.s550_chars
        elif lang == Language.BN:
            return self.bn_words, self.bn_chars
        else:
            return self.mm_words, self.mm_chars

    def load_callables(self) -> Tuple[Callable, Callable, Callable]:
        c = Correction()
        t = Transliteration()
        return c.correct, t.transliterate, t.word_map

    def load_frames(self):
        correct, transliterate, word_map = self.load_callables()
        self.text_tab = TestFrame(self, correct, transliterate, word_map)
        self.analyze_tab_s550 = AnalyzeFrame(
            self, self.s550_words, self.s550_chars, True
        )
        self.analyze_tab_bn = AnalyzeFrame(self, self.bn_words, self.bn_chars)
        self.analyze_tab_mm = AnalyzeFrame(self, self.mm_words, self.mm_chars)
        self.add(self.text_tab, text="Test")
        self.add(self.analyze_tab_s550, text="S-550")
        self.add(self.analyze_tab_bn, text="Bengali")
        self.add(self.analyze_tab_mm, text="Meetei Mayek")
