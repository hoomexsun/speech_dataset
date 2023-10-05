import tkinter as tk
import sv_ttk
from src.gui import MainFrame


class App:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Speech Dataset GUI")
        self.root.geometry(center_window(root, 1280, 720))
        self.root.resizable(False, False)
        self.tab_layout = MainFrame(root)


def center_window(root, width, height) -> str:
    x = (root.winfo_screenwidth() - width) // 2
    return f"{width}x{height}+{x}+0"


def gui():
    root = tk.Tk()
    sv_ttk.set_theme("light")
    app = App(root)
    print("GUI running...")
    root.mainloop()


if __name__ == "__main__":
    gui()
