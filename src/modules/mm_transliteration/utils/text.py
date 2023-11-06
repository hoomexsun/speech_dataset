import io
from typing import Dict, List

import pyperclip


# String Level text processing functions.
def remove_chars(content: str, chars: List[str]) -> str:
    for char in chars:
        content = content.replace(char, "")
    return content


def replace_chars(content: str, charmap: Dict[str, str]) -> str:
    for char, replacement in charmap.items():
        content = content.replace(char, replacement)
    return content


def fix_mistypes(content: str, chars: List[str], num_mistypes: int = 2) -> str:
    for char in chars:
        for num in range(num_mistypes + 1, 1, -1):
            content = content.replace(char * num, char)
    return content


def get_unicode_string(content: str, skip_newline: bool = False) -> str:
    ss = io.StringIO()
    for char in content:
        if char == "\n" and skip_newline:
            ss.write("\n")
        else:
            try:
                ss.write("\\u" + format(ord(char), "x").zfill(4))
            except UnicodeEncodeError:
                ss.write("\\x" + char.encode("utf-8").hex())
    return ss.getvalue()


# 3rd party
def copy_text(char) -> None:
    pyperclip.copy(char)


# Calculation
def pct(num: int, total: int) -> str:
    """Calculate the percentage.

    Args:
        num (int): Numerator value.
        total (int): Total value.

    Returns:
        str: Percentage value formatted as a string with two decimal places.
    """
    return format(100 * num / total, ".2f")
