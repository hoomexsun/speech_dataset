import tkinter as tk
from typing import Collection, List
from tkinter import ttk, font
from src.core.analysis import generate_char_dictionary
from src.utils.fonts.font_loader import loadfont
from src.utils.text import get_unicode_string

DELIMITER = "DEL"


class AnalyzeFrame(ttk.Frame):
    def __init__(
        self,
        parent: tk.Misc | None,
        words: List[str],
        chars: List[str],
        glyph_mode: bool = False,
        width: int = 1280,
        height: int = 720,
    ):
        super().__init__(parent)
        self._parent = parent
        self._words = words
        self._chars = chars
        self._glyph_mode = glyph_mode
        self._width = width
        self._height = height
        self._init_variables()
        self._init_ui()

    def _init_variables(self):
        loadfont("utils/fonts/S-550.ttf")
        self._custom_font = font.Font(family="S-550", size=18)
        self._default_font = font.nametofont("TkDefaultFont")
        self._text = tk.StringVar()
        self._text.trace("w", self.on_input_change)
        self._use_custom_font = True if self._glyph_mode else False
        self._analyze_mode = True
        self._matched_words: list = []
        self._current_page = 0
        self._items_per_page = self.update_items_per_page()
        self._num_matches = tk.IntVar()
        self._num_words = tk.IntVar()
        self._results_var = tk.StringVar(value=f"Not searching at the moment...")
        self._undo_state = False

    # UI
    def _init_ui(self):
        input_frame_width = 550
        output_frame_width = self._width - input_frame_width
        self._add_input_components(
            x=0, y=0, width=input_frame_width, height=self._height
        )
        self._add_output_components(
            x=input_frame_width, y=0, width=output_frame_width, height=self._height
        )

    def _add_input_components(self, x, y, width=500, height=720):
        self.input_frame = ttk.LabelFrame(self, text="Search/Analyze words")
        self.input_frame.place(
            x=x,
            y=y,
            width=width,
            height=height,
        )
        x, y, width, height = 10, 10, width - 20, height - 20
        self.input_entry = ttk.Entry(
            self.input_frame, textvariable=self._text, state=self.is_go_disabled()
        )
        self.input_entry.place(x=x, y=y, width=240)

        self.go_button = ttk.Button(
            self.input_frame,
            text="Go",
            command=self.go_char,
            state=self.is_go_disabled(),
        )
        self.go_button.place(x=255, y=y, width=90)

        self.font_button = ttk.Button(
            self.input_frame,
            text=self.update_font_text(),
            command=self.toggle_font,
            state=self.is_glyph_used(),
        )
        self.font_button.place(x=350, y=y, width=90)

        self.mode_button = ttk.Button(
            self.input_frame,
            text=self.update_mode_text(),
            command=self.toggle_mode,
        )
        self.mode_button.place(x=445, y=y, width=90)

        self.prev_btn = ttk.Button(
            self.input_frame, text="Prev", command=self.prev_page
        )
        self.prev_btn.place(x=350, y=y + 35, width=90)

        self.next_btn = ttk.Button(
            self.input_frame, text="Next", command=self.next_page
        )
        self.next_btn.place(x=445, y=y + 35, width=90)

        num_results_label = ttk.Label(self.input_frame, textvariable=self._results_var)
        num_results_label.place(x=x, y=y + 35)

        self.current_page_label = ttk.Label(self.input_frame, text="Page: 1")
        self.current_page_label.place(x=x, y=y + 60)

        self._input_grid(self.input_frame, x=x, y=y + 85, items=self._chars)

    def _add_output_components(self, x, y, width, height):
        self._output_frame = tk.Frame(self)
        self._output_frame.place(x=x, y=y, width=width, height=height)
        x, y, width, height = 10, 10, width - 20, height - 20

    def _input_grid(
        self,
        parent,
        x: int,
        y: int,
        items: Collection,
        num_columns=12,
        item_width=40,
        item_height=30,
    ):
        x_offset, y_offset = item_width + 5, item_height + 5
        for idx, char in enumerate(items):
            y_multiplier, x_multiplier = divmod(idx, num_columns)
            btn = ttk.Button(
                parent,
                text=char,
                command=lambda c=char: self.go_char(c),
            )
            btn.place(
                x=x + x_offset * x_multiplier,
                y=y + y_offset * y_multiplier,
                width=item_width,
                height=item_height,
            )

    def _search_grid(
        self,
        parent,
        x,
        y,
        items,
        num_columns=5,
        item_width=35,
        item_height=30,
    ):
        x_offset, y_offset = item_width + 5, item_height + 5
        for idx, char in enumerate(items):
            y_multiplier, x_multiplier = divmod(idx, num_columns)
            word_label = ttk.Label(
                parent,
                text=char,
            )
            word_label.place(
                x=x + x_offset * x_multiplier,
                y=y + y_offset * y_multiplier,
                width=item_width,
                height=item_height,
            )
        self.on_font_toggle()

    def _analysis_grid(
        self,
        parent,
        x,
        y,
        items,
        num_columns=6,
        item_width=35,
        item_height=30,
    ):
        x_offset, y_offset = item_width + 5, item_height + 5
        style = ttk.Style()
        style.configure("LeftAligned.TButton", anchor="w")
        for idx, char in enumerate(items):
            rank, comb, count = char.split(DELIMITER)
            y_multiplier, x_multiplier = divmod(idx, num_columns)
            comb_btn = ttk.Button(
                parent,
                text=f"{rank}. {comb} ({count})",
                style="LeftAligned.TButton",
                command=lambda c=comb: self.go_output(c),
                # command=lambda c=comb: copy_text(c),
            )
            comb_btn.place(
                x=x + x_offset * x_multiplier,
                y=y + y_offset * y_multiplier,
                width=item_width - 60 if self._glyph_mode else item_width,
                height=item_height,
            )
            if self._glyph_mode:
                word_label = ttk.Label(
                    parent,
                    text=comb,
                )
                word_label.place(
                    x=x + x_offset * x_multiplier + 120,
                    y=y + y_offset * y_multiplier,
                    width=50,
                    height=item_height,
                )
        self.on_font_toggle()

    # Reset UI
    def hard_reset_ui(self) -> None:
        self._matched_words = []
        self.reset_ui()

    def reset_ui(self) -> None:
        # Option 1: Generic
        for widget in self._output_frame.winfo_children():
            widget.destroy()
        # Option 2: Specific
        # for widget in self._output_frame.winfo_children():
        #     if isinstance(widget, ttk.Label) or isinstance(widget, ttk.Button):
        #         widget.destroy()

    # Commands
    def toggle_font(self) -> None:
        self._use_custom_font = not self._use_custom_font
        self.on_font_toggle()

    def toggle_mode(self) -> None:
        self._analyze_mode = not self._analyze_mode
        self.on_mode_toggle()
        if not len(self._text.get()) == 0:
            self.go()

    def go_char(self, input: str | None = None) -> None:
        self.hard_reset_ui()
        self._text.set(self._text.get() if input == None else input)
        self.go()

    def go_output(self, comb: str) -> None:
        self.go_char(comb)
        self.toggle_mode()

    def prev_page(self):
        if self._current_page > 0:
            self._current_page -= 1
            self.reload_results()

    def next_page(self):
        total_pages = len(self._matched_words) // self._items_per_page
        if self._current_page < total_pages:
            self._current_page += 1
            self.reload_results()

    # Reactivity
    def update_font_text(self) -> str:
        return "Glyph" if self._use_custom_font else "Unicode"

    def update_mode_text(self) -> str:
        return "Analyze" if self._analyze_mode else "Search"

    def update_items_per_page(self) -> int:
        return 76 if self._analyze_mode else 95

    def is_undo_availabe(self) -> str:
        return tk.NORMAL if self._undo_state else tk.DISABLED

    def is_glyph_used(self) -> str:
        return tk.NORMAL if self._glyph_mode else tk.DISABLED

    def is_input_disabled(self) -> str:
        return tk.DISABLED if self._analyze_mode else tk.NORMAL

    def is_go_disabled(self) -> str:
        return (
            tk.DISABLED
            if self._analyze_mode or len(self._text.get()) == 0
            else tk.NORMAL
        )

    def is_prev_disabled(self) -> str:
        total_pages = len(self._matched_words) // self._items_per_page
        return tk.DISABLED if total_pages == 0 or self._current_page == 0 else tk.NORMAL

    def is_next_disabled(self) -> str:
        total_pages = len(self._matched_words) // self._items_per_page
        return (
            tk.DISABLED
            if total_pages == 0 or self._current_page == total_pages
            else tk.NORMAL
        )

    # * Not every change occurs because of click events, these are reusable functions
    # * which can responds to other events in addition to click events
    def on_input_change(self, *args) -> None:
        self.input_entry["state"] = self.is_input_disabled()
        self.go_button["state"] = self.is_go_disabled()

    def on_page_navigate(self) -> None:
        self.prev_btn["state"] = self.is_prev_disabled()
        self.next_btn["state"] = self.is_next_disabled()
        total_pages = len(self._matched_words) // self._items_per_page
        current_page_number = self._current_page + 1
        start_idx = self._current_page * self._items_per_page
        end_idx = start_idx + min(
            len(self._matched_words) - start_idx, self._items_per_page
        )
        result_range = (
            "0 results."
            if end_idx == 0
            else f"{start_idx + 1}-{end_idx} out of {len(self._matched_words)} results."
        )
        self.current_page_label.config(
            text=f"Page: {current_page_number}/{total_pages + 1} | Showing {result_range}"
        )

    def on_font_toggle(self) -> None:
        self.font_button["text"] = self.update_font_text()
        for label in self._output_frame.winfo_children():
            if isinstance(label, ttk.Label):
                if self._use_custom_font:
                    label.configure(font=self._custom_font)
                else:
                    label.configure(font=self._default_font)

    def on_mode_toggle(self) -> None:
        self.on_input_change()
        self.mode_button["text"] = self.update_mode_text()
        self._items_per_page = self.update_items_per_page()

    def on_result_change(self) -> None:
        result_text = f"Found {self._text.get()} ({get_unicode_string(self._text.get())}) in {self._num_matches.get()} "
        if self._analyze_mode:
            result_text += f"combinations."
        else:
            result_text += f"words out of {len(self._words)}."
        self._results_var.set(result_text)

    # Functionality
    def go(self) -> None:
        self.reset_ui()
        # Analyze Mode or Search Mode
        self._matched_words = (
            [
                f"{idx+1}{DELIMITER}{word}{DELIMITER}{count}"
                for idx, (word, count) in enumerate(
                    generate_char_dictionary(
                        char=self._text.get(), words=self._words
                    ).items()
                )
            ]
            if self._analyze_mode
            else [word for word in self._words if self._text.get() in word]
        )
        self._current_page = 0
        self._num_matches.set(len(self._matched_words))
        self.on_result_change()
        self.reload_results()

    # Pagination
    def reload_results(self) -> None:
        self._num_words.set(len(self._matched_words))
        start_idx = self._current_page * self._items_per_page
        end_idx = start_idx + self._items_per_page
        displayed_words = self._matched_words[start_idx:end_idx]
        x, y = 10, 10
        self.reset_ui()
        if self._output_frame:
            if self._analyze_mode:
                self._analysis_grid(
                    self._output_frame,
                    x=x,
                    y=y,
                    items=displayed_words,
                    num_columns=4,
                    item_width=170,
                )
            else:
                self._search_grid(
                    self._output_frame,
                    x=x,
                    y=y,
                    items=displayed_words,
                    num_columns=5,
                    item_width=140,
                )
        self.on_page_navigate()
