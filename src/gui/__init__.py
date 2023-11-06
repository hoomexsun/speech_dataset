from tkinter import Misc, ttk
import tkinter as tk
from typing import Callable, List, Tuple
from config import (
    Language,
    CHARS_BN_FILE,
    CHARS_MM_FILE,
    CHARS_S550_FILE,
    WORDS_BN_FILE,
    WORDS_MM_FILE,
    WORDS_S550_FILE,
)
from src.modules.glyph_correction import GlyphCorrection
from src.modules.mm_transliteration import MMTransliteration
from src.utils.file import read_list
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
        self.s550_words = read_list(WORDS_S550_FILE)
        self.bn_words = read_list(WORDS_BN_FILE)
        self.mm_words = read_list(WORDS_MM_FILE)
        self.s550_chars = read_list(CHARS_S550_FILE)
        self.bn_chars = read_list(CHARS_BN_FILE)
        self.mm_chars = read_list(CHARS_MM_FILE)

    def reload_content(self, lang: Language) -> Tuple[List[str], List[str]]:
        if lang == Language.S550:
            return self.s550_words, self.s550_chars
        elif lang == Language.BN:
            return self.bn_words, self.bn_chars
        else:
            return self.mm_words, self.mm_chars

    def load_callables(self) -> Tuple[Callable, Callable]:
        c = GlyphCorrection()
        t = MMTransliteration()
        return c.correct, t.transliterate

    def load_frames(self):
        correct, transliterate = self.load_callables()
        self.text_tab = TestFrame(self, correct, transliterate)
        self.analyze_tab_s550 = AnalyzeFrame(
            self, self.s550_words, self.s550_chars, True
        )
        self.analyze_tab_bn = AnalyzeFrame(self, self.bn_words, self.bn_chars)
        self.analyze_tab_mm = AnalyzeFrame(self, self.mm_words, self.mm_chars)
        self.add(self.text_tab, text="Test")
        self.add(self.analyze_tab_s550, text="S-550")
        self.add(self.analyze_tab_bn, text="Bengali")
        self.add(self.analyze_tab_mm, text="Meetei Mayek")
