import tkinter as tk
from tkinter import ttk
import sv_ttk
from steps.res import init_resources
from utils.gui.analyze_frame import AnalyzeFrame
from utils.gui.test_frame import TestFrame


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech Dataset GUI")
        self.root.geometry("1280x720")
        self.root.resizable(False, False)

        self.tab_layout = ttk.Notebook(root)
        self.tab_layout.pack(fill=tk.BOTH, expand=True)

        self.text_tab = TestFrame(self.tab_layout)
        self.analyze_tab = AnalyzeFrame(self.tab_layout)

        self.tab_layout.add(self.text_tab, text="Test")
        self.tab_layout.add(self.analyze_tab, text="Analyze")


if __name__ == "__main__":
    init_resources()
    root = tk.Tk()
    sv_ttk.set_theme("light")
    app = App(root)
    root.mainloop()
