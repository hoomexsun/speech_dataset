import tkinter as tk
from tkinter import ttk
from transliteration import Transliteration
from correction import Correction
from utils.gui_units import CustomButton, TestItem
from config.paths import *
import sv_ttk


class APP(tk.Frame):
    def __init__(self, master) -> None:
        """
        Initialize the GUI_MODE class.

        Args:
            master (optional): The parent widget.

        Returns:
            None
        """
        tk.Frame.__init__(self, master=master)
        self._master = master
        self.init_variables()
        self.init_window()

    def init_variables(self) -> None:
        """
        Initialize the variables.

        Returns:
            None
        """
        self._output_type = [
            "BN (s550 Correction)",
            "MM (Rule-based Transliteration)",
            "MM (WordMap using Dictionary)",
            "MM -> Phoneme (G2P)",
        ]
        self.c = Correction()
        self.t = Transliteration()

    def init_window(self) -> None:
        """
        Initialize the window and its components.

        Returns:
            None
        """
        start_x, start_y = 20, 20
        input_frame_width, output_frame_width = 220, 640
        input_frame_height, output_frame_height = 540, 540

        # Setup LabelFrame for Input
        x, y = start_x, start_y  # init

        input_label_frame = ttk.LabelFrame(self.master, text="INPUT")
        input_label_frame.propagate(True)
        input_label_frame.place(
            x=20, y=30, width=input_frame_width, height=input_frame_height
        )

        self.__string_input = TestItem(
            input_label_frame, "Input String", x, y, vertical=True
        )
        self.__string_input.set_values("¹à\\¸šàº JåàÒüƒà ")

        y += 220
        correct_button = CustomButton(
            input_label_frame, "Correct s550", x, y, self.gui_correct
        )
        y += 35
        exec_xlit_button = CustomButton(
            input_label_frame, "Transliterate BN", x, y, self.gui_transliterate
        )
        y += 35
        exec_xlit_and_xform_button = CustomButton(
            input_label_frame,
            "Transliterate s550",
            x,
            y,
            self.gui_correct_and_transliterate,
        )
        y += 35
        exec_mm_g2p_button = CustomButton(
            input_label_frame, "Generate Phoneme", x, y, self.gui_mm_g2p
        )

        y += 20  # gap
        y += 35
        reset_button = CustomButton(input_label_frame, "Reset all", x, y, self.reset)
        y += 35
        toggle_button = CustomButton(
            input_label_frame, "Toggle Theme", x, y, self.toggle_theme
        )
        y += 35
        exit = CustomButton(input_label_frame, "Exit", x, y, self.exit)

        # Setup LabelFrame for Output
        x, y = start_x + input_frame_width + 20, start_y  # Init
        self._output_label_frame = ttk.LabelFrame(self.master, text="OUTPUT")
        # self._output_label_frame.propagate(True)
        self._output_label_frame.place(
            x=x, y=y, width=output_frame_width, height=output_frame_height
        )

        self.__output = []

        x = start_x
        y = y
        self._text_bn = TestItem(self._output_label_frame, self._output_type[0], x, y)
        self.__output.append(self._text_bn)

        y += 120
        self._text_mm_algo = TestItem(
            self._output_label_frame, self._output_type[1], x, y
        )
        self.__output.append(self._text_mm_algo)

        y += 120
        self._text_mm_wmap = TestItem(
            self._output_label_frame, self._output_type[2], x, y
        )
        self.__output.append(self._text_mm_wmap)

        y += 120
        self._text_mm_g2p = TestItem(
            self._output_label_frame, self._output_type[3], x, y
        )
        self.__output.append(self._text_mm_g2p)

        self._result_text_field = [
            self.__string_input,
            self._text_bn,
            self._text_mm_algo,
            self._text_mm_wmap,
            self._text_mm_g2p,
        ]

    def fix_input(self):
        self.__string_input.set_values(self.__string_input.get_text_value())

    def reset(self, soft=False) -> None:
        """
        Reset the GUI:
        1.  Clear all input in the textfield.

        Args:
            soft (optional): A boolean indicating if it's a soft reset or not.

        Returns:
            None
        """
        print("Reset")
        if not soft:
            self.__string_input.reset()
        self._text_bn.reset()
        self._text_mm_algo.reset()
        self._text_mm_wmap.reset()
        self._text_mm_g2p.reset()
        self._test_result = []
        self._test_string = []

    def exit(self) -> None:
        """
        Exit this program normally

        Returns:
            None
        """
        print("Exit")
        exit(0)

    def gui_correct(self) -> None:
        """
        Perform the transformation operation in the GUI.

        Returns:
            None
        """
        print("called gui_correct")
        self.fix_input()
        text = self.__string_input.get_text_value()
        self.reset(True)
        self._text_bn.set_values(self.c.correct(text))

    def gui_transliterate(self) -> None:
        """
        Perform the transliteration operation in the GUI.

        Returns:
            None
        """
        print("Called gui_transliterate")
        self.fix_input()
        text = self.__string_input.get_text_value()
        self.reset(True)
        self._text_mm_algo.set_values(self.t.transliterate(text))
        self._text_mm_wmap.set_values(self.gui_wmap(text))

    def gui_correct_and_transliterate(self) -> None:
        """
        Perform the transformation and transliteration operations in the GUI.

        Returns:
            None
        """
        print("Called gui_correct_and_transliterate")
        self.fix_input()
        text = self.__string_input.get_text_value()
        self.reset(True)
        str_bn = self.c.correct(text)
        self._text_bn.set_values(str_bn)
        self._text_mm_algo.set_values(self.t.transliterate(str_bn))
        self._text_mm_wmap.set_values(self.gui_wmap(str_bn))

    def gui_wmap(self, text) -> str:
        """
        Apply word mapping to the given text.

        Args:
            text: The input text.

        Returns:
            The text after word mapping.
        """
        print("Called gui_wmap")
        self.fix_input()
        return self.t.word_map(text)

    def gui_mm_g2p(self) -> None:
        """
        Perform the G2P operation for Meetei Mayek in the GUI.

        Returns:
            None
        """
        print("Called gui_mm_g2p")
        self.fix_input()
        pass

    def toggle_theme(self):
        if sv_ttk.get_theme() == "dark":
            print("Setting theme to light")
            sv_ttk.use_light_theme()
        elif sv_ttk.get_theme() == "light":
            print("Setting theme to dark")
            sv_ttk.use_dark_theme()
        else:
            print("Not Sun Valley theme")


def gui() -> None:
    """
    Start the GUI application.

    Returns:
        None
    """
    root = tk.Tk()
    sv_ttk.set_theme("dark")
    root.title("speech_dataset: GUI Mode")
    root.geometry("%dx%d+0+0" % (920, 600))
    root.resizable(False, False)
    root.update()
    app = APP(root)
    app.mainloop()


# -------------------------------- SCRIPT MODE -------------------------------- #
if __name__ == "__main__":
    gui()
