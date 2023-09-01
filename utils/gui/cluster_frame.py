import tkinter as tk
from typing import Dict, List, Tuple
from tkinter import ttk, font
from utils.file import fread
from utils.fonts.font_loader import loadfont
from collections import defaultdict


# TODO: Make a Frame to find cluster containing a character or a group of character.
# TODO: Also arrange the clusters with number of occurence and a copy button.
# TODO: Add for all three character sets.o
class ClusterFrame(ttk.Frame):
    def __init__(
        self,
        parent: tk.Misc | None,
        words: List[str],
        chars: List[str],
        width: int = 1280,
        height: int = 720,
    ):
        super().__init__(parent)
        self.words = words
        self.chars = chars
        self.width = width
        self.height = height
        self.__init_variables()
        input_frame_width = 500
        output_frame_width = self.width - input_frame_width
        self.add_input_components(x=0, y=0, width=input_frame_width, height=self.height)
        self.add_output_components(
            x=input_frame_width, y=0, width=output_frame_width, height=self.height
        )

    def __init_variables(self):
        self._items_per_page = 95
        self._current_page = 0

        self.default_font = font.nametofont("TkDefaultFont")
        loadfont("utils/fonts/S-550.ttf")
        self.custom_font = font.Font(family="S-550", size=18)
        self._input = tk.StringVar()
        self._use_custom_font = False
        self._chars: list = []
        self._words: list = []
        self._matched_words: list = []
        self._num_combination = tk.IntVar()
        self._search_results = tk.StringVar(value=f"Start searching...")

    def add_input_components(self, x, y, width=500, height=720):
        self.input_frame = ttk.LabelFrame(self, text="Search words with character")
        self.input_frame.place(
            x=x,
            y=y,
            width=width,
            height=height,
        )
        x, y, width, height = 10, 10, width - 20, height - 20
        input_entry = ttk.Entry(self.input_frame, textvariable=self._input)
        input_entry.place(x=x, y=y, width=240)

        search_button = ttk.Button(self.input_frame, text="Search", command=self.search)
        search_button.place(x=255, y=y, width=115)

        toggle_button = ttk.Button(
            self.input_frame, text="Toggle", command=self.change_font
        )
        toggle_button.place(x=375, y=y, width=115)

        num_results_label = ttk.Label(
            self.input_frame, textvariable=self._search_results
        )
        num_results_label.place(x=x, y=y + 35)

        prev_btn = ttk.Button(self.input_frame, text="Prev", command=self.prev)
        prev_btn.place(x=255, y=y + 35, width=115)

        next_btn = ttk.Button(self.input_frame, text="Next", command=self.next)
        next_btn.place(x=375, y=y + 35, width=115)

        self.current_page_label = ttk.Label(self.input_frame, text="Page: 1")
        self.current_page_label.place(x=x, y=y + 60)

        self.input_grid(
            self.input_frame,
            x=x,
            y=y + 85,
            items=self._chars,
            func=self.search_from_btn,
        )

    def add_output_components(self, x, y, width, height):
        self._output_frame = tk.Frame(self)
        self._output_frame.place(x=x, y=y, width=width, height=height)

        x, y, width, height = 10, 10, width - 20, height - 20
        self.reload_matched_words()

    # Search Functionality
    def search_from_btn(self, char):
        self._input.set(char)
        self.search()

    def search(self):
        self.reset_matched_words()
        self._matched_words = [
            word for word in self._words if self._input.get() in word
        ].copy()
        self._current_page = 0  # Reset to the first page
        self.reload_matched_words()
        self._num_combination.set(len(self._matched_words))
        self._search_results.set(
            f"Found {self._num_combination.get()} words out of {len(self._words)}."
        )

    def reload_matches(
        self, target: str
    ) -> Tuple[
        int, int, int, Dict[str, int], Dict[str, int], Dict[Tuple[str, str], int]
    ]:
        matched_words = [word for word in self.words if target in word]
        num_matches = len(matched_words)

        with_prefix: Dict[str, int] = defaultdict(int)
        with_suffix: Dict[str, int] = defaultdict(int)
        with_both: Dict[Tuple[str, str], int] = defaultdict(int)

        for word in matched_words:
            for i in range(len(word) - len(target) + 1):
                if word[i : i + len(target)] == target:
                    prefix = word[i - 1 : i] if i > 0 else ""
                    suffix = (
                        word[i + len(target) : i + len(target) + 1]
                        if i + len(target) < len(word)
                        else ""
                    )

                    with_prefix[prefix] += bool(prefix)
                    with_suffix[suffix] += bool(suffix)
                    with_both[(prefix, suffix)] += bool(prefix and suffix)

        at_begin: int = sum(1 for word in matched_words if word.startswith(target))
        at_end: int = sum(1 for word in matched_words if word.endswith(target))
        at_middle: int = sum(1 for word in matched_words if target in word[1:-1])

        return at_begin, at_end, at_middle, with_prefix, with_suffix, with_both

    def reload_matched_words(self):
        start_idx = self._current_page * self._items_per_page
        end_idx = start_idx + self._items_per_page
        displayed_words = self._matched_words[start_idx:end_idx]

        x, y = 10, 10
        if self._output_frame:
            self.output_grid(
                self._output_frame,
                x=x,
                y=y,
                items=displayed_words,
                num_columns=5,
                item_width=140,
            )
        self.update_current_page_label()

    def update_current_page_label(self):
        total_pages = len(self._matched_words) // self._items_per_page
        current_page_number = self._current_page + 1  # Pages are 1-indexed

        start_idx = self._current_page * self._items_per_page
        end_idx = start_idx + min(
            len(self._matched_words) - start_idx, self._items_per_page
        )

        self.current_page_label.config(
            text=f"Page: {current_page_number}/{total_pages + 1} | Matches: {start_idx + 1}-{end_idx} out of {len(self._matched_words)}"
        )

    def prev(self):
        if self._current_page > 0:
            self._current_page -= 1
            self.reload_matched_words()
            self.update_current_page_label()

    def next(self):
        total_pages = len(self._matched_words) // self._items_per_page
        if self._current_page < total_pages:
            self._current_page += 1
            self.reload_matched_words()
            self.update_current_page_label()

    # Grids
    def input_grid(
        self, parent, x, y, items, func, num_columns=12, item_width=35, item_height=30
    ):
        x_offset, y_offset = item_width + 5, item_height + 5
        for idx, char in enumerate(items):
            y_multiplier, x_multiplier = divmod(idx, num_columns)
            btn = ttk.Button(
                parent,
                text=char,
                command=lambda c=char: func(c),
            )
            btn.place(
                x=x + x_offset * x_multiplier,
                y=y + y_offset * y_multiplier,
                width=item_width,
                height=item_height,
            )

    def output_grid(
        self,
        parent,
        x,
        y,
        items,
        num_columns=12,
        item_width=35,
        item_height=30,
    ):
        x_offset, y_offset = item_width + 5, item_height + 5
        for idx, char in enumerate(items):
            y_multiplier, x_multiplier = divmod(idx, num_columns)
            btn = ttk.Label(
                parent,
                text=char,
            )
            btn.place(
                x=x + x_offset * x_multiplier,
                y=y + y_offset * y_multiplier,
                width=item_width,
                height=item_height,
            )

    # Resets
    def reset_matched_words(self):
        self._matched_words = []
        for label in self._output_frame.winfo_children():
            if isinstance(label, ttk.Label):
                label.destroy()

    #! Only works for windows
    def change_font(self):
        self._use_custom_font = not self._use_custom_font
        for label in self._output_frame.winfo_children():
            if isinstance(label, ttk.Label):
                if self._use_custom_font:
                    label.configure(font=self.custom_font)
                else:
                    label.configure(font=self.default_font)
