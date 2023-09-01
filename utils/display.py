from pathlib import Path
from config.project import format_msg
from utils.file import fread
from utils.text import get_unicode_string, unicode_as_df


def display_unicode_counts_in_file(file_path: Path):
    data = fread(file_path)
    df = unicode_as_df(content=data)
    print(df)


def display_unicode(content: str) -> None:
    print(get_unicode_string(content=content))


def display_line(title: str, target: str, desc: str):
    """Display a formatted line with information.

    Args:
        title (str, optional): Title for the line. Defaults to "".
        target (str, optional): Target information for the line. Defaults to "".
        suffix (str, optional): Suffix information for the line. Defaults to "".
        idx (int, optional): Index information for the line. Defaults to -1.
    """
    print(format_msg(title=title, target=target, desc=desc))
