import tkinter as tk
from tkinter import ttk
import pyperclip
from config.paths import *
from utils.text import get_unicode_string, unicode_as_df


class TestItem:
    def __init__(self, parent: tk.Misc | None, title: str, x: int, y: int) -> None:
        self._text = tk.StringVar()
        self._num_chars = tk.IntVar()
        self._unicode = tk.StringVar()

        self._text.trace("w", self.on_text_change)

        x_var, y_var = x, y
        width, info_width, count_width = 180, 700, 40
        second_part_height = 80
        label_height = 25

        label = ttk.Label(parent, text=title)
        label.place(x=x_var, y=y_var, height=label_height)

        text_entry = ttk.Entry(parent, textvariable=self._text)
        text_entry.place(x=x_var, y=y_var + 30, width=width - count_width, height=25)

        count_char_entry = ttk.Entry(parent, textvariable=self._num_chars)
        count_char_entry.config(state=tk.DISABLED)
        count_char_entry.place(
            x=x_var + width - count_width, y=y_var + 30, width=count_width
        )

        self.reset_btn = ttk.Button(
            parent, text="RESET", command=self.reset, state=tk.DISABLED
        )
        self.reset_btn.place(x=x, y=y_var + 30 + 30, width=width // 2)

        self.copy_btn = ttk.Button(
            parent, text="COPY", command=self.copy, state=tk.DISABLED
        )
        self.copy_btn.place(
            x=x + width // 2,
            y=y_var + 30 + 30,
            width=width // 2,
        )

        unicode_entry = tk.Label(
            parent,
            textvariable=self._unicode,
            anchor=tk.W,
            wraplength=info_width,
        )
        unicode_entry.place(
            x=200,
            y=y + label_height + 5,
            width=info_width,
            height=second_part_height,
        )

    def on_text_change(self, *args):
        if len(self._text.get()) == 0:
            self.reset_btn["state"] = tk.DISABLED
            self.copy_btn["state"] = tk.DISABLED
        else:
            self.reset_btn["state"] = tk.NORMAL
            self.copy_btn["state"] = tk.NORMAL

    @property
    def text(self) -> str:
        return self._text.get()

    @text.setter
    def text(self, value: str) -> None:
        self._text.set(value)

    def set_num_chars(self, value: int) -> None:
        self._num_chars.set(value)

    def _get_unicode(self, text: str) -> str:
        return get_unicode_string(text)

    def set_unicode_value(self, value: str) -> None:
        self._unicode.set(value)

    def set_values(self, text: str) -> None:
        self._text.set(text)
        self._num_chars.set(len(text))
        self._unicode.set(self._get_unicode(text))
        # self._get_unicode_info(text)

    def reset(self) -> None:
        self.set_num_chars(0)
        self.text = ""
        self.set_unicode_value("")

    def copy(self) -> None:
        pyperclip.copy(self.text)

    def _get_unicode_info(self, text: str) -> None:
        if self.text != "":
            df = unicode_as_df(text)
            unicodes = df.loc[:, "unicode"]
            counts = df.loc[:, "count"]
            max_num = int(unicodes.count())


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Enable mouse scrolling
        self.canvas.bind("<Enter>", self._bind_mousewheel)
        self.canvas.bind("<Leave>", self._unbind_mousewheel)

    def _bind_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * int(event.delta / 120), "units")


# Functions
Y_OFFSET = 35
GAP = 20
TEST_ITEM_HEIGHT = 120


def y_var(a: int = 0, b: int = 0) -> int:
    return 10 + Y_OFFSET * a + GAP * b


def y_var_out(a: int = 0) -> int:
    return 10 + TEST_ITEM_HEIGHT * a
