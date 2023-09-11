from typing import Callable
import sv_ttk
import tkinter as tk
from tkinter import ttk
from src.gui.widgets import TestItem, y_var, y_var_out


ITEM_WIDTH = 200


class TestFrame(ttk.Frame):
    def __init__(
        self,
        parent,
        correct: Callable,
        transliterate: Callable,
        word_map: Callable,
        width: int = 1280,
        height: int = 720,
    ):
        super().__init__(parent)
        self._parent = parent
        self.correct = correct
        self.transliterate = transliterate
        self.word_map = word_map
        self.width = width
        self.height = height
        self._init_variables()
        input_frame_width = 220
        output_frame_width = width - input_frame_width
        self.add_input_components(x=0, y=0, width=input_frame_width, height=self.height)
        self.add_output_components(
            x=input_frame_width, y=0, width=output_frame_width, height=self.height
        )

    def _init_variables(self) -> None:
        self._text = tk.StringVar()
        self._output_functions = []
        self._output_titles = [
            "BN (s550 Correction)",
            "MM (Rule-based Transliteration)",
            "MM (WordMap using Dictionary)",
            "MM -> Phoneme (G2P)",
        ]

    def add_input_components(self, x, y, width, height):
        self.input_frame = ttk.LabelFrame(self, text="INPUT")
        self.input_frame.place(
            x=x,
            y=y,
            width=width,
            height=height,
        )
        x, y = 10, 10

        text_entry = ttk.Entry(self.input_frame, textvariable=self._text)
        self._text.set("¹à\\¸šàº JåàÒüƒà")
        text_entry.place(x=x, y=y_var(), width=ITEM_WIDTH)

        correct_btn = ttk.Button(
            self.input_frame, text="Correct s550", command=self.gui_correct
        )
        correct_btn.place(x=x, y=y_var(1, 1), width=ITEM_WIDTH)
        transliterate_btn = ttk.Button(
            self.input_frame, text="Transliterate BN", command=self.gui_transliterate
        )
        transliterate_btn.place(x=x, y=y_var(2, 1), width=ITEM_WIDTH)
        c_and_t_btn = ttk.Button(
            self.input_frame,
            text="Transliterate s550",
            command=self.gui_correct_and_transliterate,
        )
        c_and_t_btn.place(x=x, y=y_var(3, 1), width=ITEM_WIDTH)
        g2p_btn = ttk.Button(
            self.input_frame,
            text="Generate Phoneme",
            command=self.gui_mm_g2p,
            state=tk.DISABLED,
        )
        g2p_btn.place(x=x, y=y_var(4, 1), width=ITEM_WIDTH)

        clear_btn = ttk.Button(
            self.input_frame, text="Clear input", command=self.clear_input
        )
        clear_btn.place(x=x, y=y_var(5, 2), width=ITEM_WIDTH)

        reset_btn = ttk.Button(
            self.input_frame, text="Reset outputs", command=self.reset
        )
        reset_btn.place(x=x, y=y_var(6, 2), width=ITEM_WIDTH)

        toggle_btn = ttk.Button(
            self.input_frame, text="Toggle Theme", command=self.toggle_theme
        )
        toggle_btn.place(x=x, y=y_var(7, 2), width=ITEM_WIDTH)

        exit_btn = ttk.Button(self.input_frame, text="Exit", command=self.exit)
        exit_btn.place(x=x, y=y_var(8, 2), width=ITEM_WIDTH)

    def add_output_components(self, x, y, width, height):
        self._output_frame = tk.Frame(self)
        self._output_frame.place(x=x, y=y, width=width, height=height)
        x, y, width, height = 10, 10, width - 20, height - 20

        self._input_ti = TestItem(self._output_frame, "Input String", x, y=y_var_out())
        self._input_ti.set_values(self.text)

        self._bn_ti = TestItem(
            self._output_frame, self._output_titles[0], x, y=y_var_out(1)
        )
        self._output_functions.append(self._bn_ti)

        self._mm_ti_algo = TestItem(
            self._output_frame, self._output_titles[1], x, y=y_var_out(2)
        )
        self._output_functions.append(self._mm_ti_algo)

        self._mm_ti_wmap = TestItem(
            self._output_frame, self._output_titles[2], x, y=y_var_out(3)
        )
        self._output_functions.append(self._mm_ti_wmap)

        self._g2p_ti = TestItem(
            self._output_frame, self._output_titles[3], x, y=y_var_out(4)
        )
        self._output_functions.append(self._g2p_ti)

        self._result_text_field = [
            self._input_ti,
            self._bn_ti,
            self._mm_ti_algo,
            self._mm_ti_wmap,
            self._g2p_ti,
        ]

    @property
    def text(self) -> str:
        return self._text.get()

    @text.setter
    def text(self, value: str) -> None:
        self._text.set(value)

    def fix_input(self):
        self._input_ti.set_values(self.text)

    def clear_input(self):
        self.text = ""

    def reset(self, soft: bool = False) -> None:
        if not soft:
            self._input_ti.reset()
        self._bn_ti.reset()
        self._mm_ti_algo.reset()
        self._mm_ti_wmap.reset()
        self._g2p_ti.reset()
        self._test_result = []
        self._test_string = []

    def exit(self) -> None:
        print("Exit")
        exit(0)

    def gui_correct(self) -> None:
        """
        Perform the correction operation in the GUI.

        Returns:
            None
        """
        self.fix_input()
        self.reset(True)
        self._bn_ti.set_values(self.correct(self.text))

    def gui_transliterate(self) -> None:
        """
        Perform the transliteration operation in the GUI.

        Returns:
            None
        """
        self.fix_input()
        text = self.text
        self.reset(True)
        self._mm_ti_algo.set_values(self.transliterate(text))
        self._mm_ti_wmap.set_values(self.gui_wmap(text))

    def gui_correct_and_transliterate(self) -> None:
        """
        Perform the correction and transliteration operations in the GUI.

        Returns:
            None
        """
        self.fix_input()
        text = self.text
        self.reset(True)
        str_bn = self.correct(text)
        self._bn_ti.set_values(str_bn)
        self._mm_ti_algo.set_values(self.transliterate(str_bn))
        self._mm_ti_wmap.set_values(self.gui_wmap(str_bn))

    def gui_wmap(self, text) -> str:
        """
        Apply word mapping to the given text.

        Args:
            text: The input text.

        Returns:
            The text after word mapping.
        """
        self.fix_input()
        return self.word_map(text)

    def gui_mm_g2p(self) -> None:
        """
        Perform the G2P operation for Meetei Mayek in the GUI.

        Returns:
            None
        """
        self.fix_input()
        pass

    def toggle_theme(self):
        if sv_ttk.get_theme() == "dark":
            sv_ttk.use_light_theme()
        elif sv_ttk.get_theme() == "light":
            sv_ttk.use_dark_theme()
        else:
            print("Not Sun Valley theme")
