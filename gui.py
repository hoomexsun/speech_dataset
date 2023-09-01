import tkinter as tk
from tkinter import ttk
import sv_ttk
from config.paths import (
    CHARS_BN_FILE,
    CHARS_MM_FILE,
    CHARS_S550_FILE,
    WORDS_BN_FILE,
    WORDS_MM_FILE,
    WORDS_S550_FILE,
)
from steps.res import init_resources
from utils.file import fget_list
from utils.gui.analyze_frame import AnalyzeFrame
from utils.gui.cluster_frame import ClusterFrame
from utils.gui.test_frame import TestFrame


class App:
    def __init__(self, root) -> None:
        self.root = root
        self.load_content()

        self.root.title("Speech Dataset GUI")
        self.root.geometry("1280x720")
        self.root.resizable(False, False)

        self.tab_layout = ttk.Notebook(root)
        self.tab_layout.pack(fill=tk.BOTH, expand=True)

        self.text_tab = TestFrame(self.tab_layout)
        self.analyze_tab = AnalyzeFrame(self.tab_layout)
        self.cluster_tab = ClusterFrame(
            self.tab_layout, self.s550_words, self.s550_chars
        )

        self.tab_layout.add(self.text_tab, text="Test")
        self.tab_layout.add(self.analyze_tab, text="Analyze")
        self.tab_layout.add(self.cluster_tab, text="Cluster")

    def load_content(self):
        self.s550_words = fget_list(WORDS_S550_FILE)
        self.bn_words = fget_list(WORDS_BN_FILE)
        self.mm_words = fget_list(WORDS_MM_FILE)
        self.s550_chars = fget_list(CHARS_S550_FILE)
        self.bn_chars = fget_list(CHARS_BN_FILE)
        self.mm_chars = fget_list(CHARS_MM_FILE)


def gui():
    init_resources()
    root = tk.Tk()
    sv_ttk.set_theme("light")
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    gui()
