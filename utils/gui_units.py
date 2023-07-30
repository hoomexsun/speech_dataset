import tkinter as tk
from tkinter import ttk
import pyperclip
from config.paths import *
from utils.utils import Utils

FONT_NAME = "Calibri"


class CustomButton:
    """Class representing a custom button widget."""

    def __init__(
        self,
        master: tk.Misc | None,
        text: str,
        x: int,
        y: int,
        command,
        width: int = 150,
    ):
        """
        Initialize a CustomButton object.

        Args:
            master: The parent widget.
            title: The text displayed on the button.
            x: The x-coordinate of the button.
            y: The y-coordinate of the button.
            width: The width of the button.
            command: The function to be executed when the button is clicked.
        """
        button = ttk.Button(master, text=text, command=command)
        button.place(x=x, y=y, width=width, height=30)


class LabelTag:
    """Class representing a labeled tag widget."""

    def __init__(
        self,
        master: tk.Misc | None,
        title: str,
        x: int,
        y: int,
        width: int,
        font_size=18,
        border=0,
    ):
        """
        Initialize a LabelTag object.

        Args:
            master: The parent widget.
            title: The text displayed on the label.
            x: The x-coordinate of the label.
            y: The y-coordinate of the label.
            width: The width of the label.
            font_size: The font size of the label.
            border: The border width of the label.
        """
        label = ttk.Label(master, text=title)
        label.config(font=(FONT_NAME, font_size))
        label.place(x=x, y=y, width=width, height=25)


class TestItem:
    """Class representing a test item widget."""

    def __init__(
        self,
        master: tk.Misc | None,
        title: str,
        x0: int,
        y0: int,
        vertical: bool = False,
    ) -> None:
        """
        Initialize a TestItem object.

        Args:
            master: The parent widget.
            title: The title of the test item.
            x: The x-coordinate of the test item.
            y: The y-coordinate of the test item.
            bottom_x: The x-coordinate of the bottom section.
            bottom_master: The parent widget for the bottom section.
            font_size: The font size of the test item.
        """
        self.__text = tk.StringVar()
        self.__length = tk.IntVar()
        self.__unicode = tk.StringVar()
        self.s = Utils()

        start_x, start_y = 20, 20
        x, y = x0, y0
        first_part_width, second_part_width, count_width = 180, 400, 40
        second_part_height = 80
        label_height = 25

        if vertical:
            second_part_width = 180
            second_part_height = 90

        label = ttk.Label(master, text=title)
        label.config(font=(FONT_NAME, 12))
        label.place(y=y, x=x, height=label_height)

        y += 30
        text_entry = ttk.Entry(master, textvariable=self.__text)
        text_entry.place(x=x, y=y, width=first_part_width - count_width, height=25)

        x += first_part_width - count_width
        count_char_entry = ttk.Entry(master, textvariable=self.__length)
        count_char_entry.config(state=tk.DISABLED)
        count_char_entry.place(x=x, y=y, width=count_width)

        x = start_x
        y += 30
        reset_btn = CustomButton(
            master,
            text="RESET",
            x=x,
            y=y,
            command=self.reset,
            width=first_part_width // 2,
        )

        x += first_part_width // 2
        copy_btn = CustomButton(
            master,
            text="COPY",
            x=x,
            y=y,
            command=self.copy,
            width=first_part_width // 2,
        )

        if vertical:
            x = start_x
            y += 50
        else:
            x = x + 20 + first_part_width // 2
            y = y0 + +label_height + 5

        unicode_entry = tk.Label(
            master,
            textvariable=self.__unicode,
            anchor=tk.NW,
            wraplength=second_part_width,
        )
        unicode_entry.place(
            x=x, y=y, width=second_part_width, height=second_part_height
        )

    def get_text_value(self) -> str:
        """
        Get the text value of the test item.

        Returns:
            The text value.
        """
        return self.__text.get()

    def set_text_value(self, value: str) -> None:
        """
        Set the text value of the test item.

        Args:
            value: The text value to set.
        """
        self.__text.set(value)

    def set_count_char(self, value: int) -> None:
        """
        Set the count of characters in the test item.

        Args:
            value: The count value to set.
        """
        self.__length.set(value)

    def set_unicode_value(self, value: str) -> None:
        """
        Set the Unicode value of the test item.

        Args:
            value: The Unicode value to set.
        """
        self.__unicode.set(value)

    def set_values(self, text: str) -> None:
        """
        Set the values of the test item.

        Args:
            text: The text value to set.
        """
        self.__text.set(text)
        self.__length.set(len(text))
        self.__unicode.set(self.__get_unicode(text))
        self.__get_unicode_info(text)

    def reset(self) -> None:
        """Reset the test item to its initial state."""
        self.set_count_char(0)
        self.set_text_value("")
        self.set_unicode_value("")

    def copy(self) -> None:
        """Copy the text value of the test item to the clipboard."""
        pyperclip.copy(self.get_text_value())

    def __get_unicode(self, text: str) -> str:
        """
        Get the Unicode representation of the text.

        Args:
            text: The text for which to get the Unicode.

        Returns:
            The Unicode representation of the text.
        """
        return self.s.get_unicode_string(text)

    def __get_unicode_info(self, text: str) -> None:
        """
        Get the Unicode information for the text.

        Args:
            text: The text for which to get the Unicode information.
        """
        if self.get_text_value() != "":
            df = self.s.get_unicode_info_as_df(text)
            unicodes = df.loc[:, "unicode"]
            counts = df.loc[:, "count"]
            max_num = int(unicodes.count())
