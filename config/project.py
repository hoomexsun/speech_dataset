import argparse
from pathlib import Path
import io
import logging
from typing import Callable, Dict, List

from tqdm import tqdm

from config.paths import DUMP_DIR
from utils.file import change_path, fget, fwrite_text
from utils.text import utt_content_to_dict


# BaseClass
class Project:
    def __init__(
        self,
        title: str = "main",
    ) -> None:
        """Base Class.

        Args:
            title (str, optional): Title for the utility class. Defaults to "main".
        """
        self.title = title

    def __str__(self) -> str:
        return self.title


def process_directory(
    func: Callable,
    dir: Path,
    output_dir: Path = DUMP_DIR,
    desc: str = "Running...",
    return_dict: bool = False,
) -> Dict:
    content_dict = {}
    files = fget(dir=dir, extension="txt")
    for file_path in tqdm(files, total=len(files), desc=desc):
        content = func(file_path=file_path)
        fwrite_text(
            content=content,
            file_path=change_path(file_path=file_path, dir=output_dir),
        )
        if return_dict:
            content_dict.update(utt_content_to_dict(content))
    return content_dict


# Setup Logger
def setup_logger(log_file: str) -> logging.Logger:
    """
    Set up and configure a logger.

    Args:
        log_file (str): The name of the log file

    Returns:
        logging.Logger: A configured logger object
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(message)s")
    file_handler = logging.FileHandler(log_file, mode="w")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


# Setup ArgumentParser: Use only for complex parser
def setup_arg_parser(description: str, arguments: List) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    for arg_info in arguments:
        name = arg_info["name"]
        flags = arg_info["flags"]
        help_text = arg_info["help"]
        arg_type = arg_info.get("type", str)
        default_value = arg_info.get("default", None)
        required = arg_info.get("required", False)

        parser.add_argument(
            *flags,
            dest=name,
            type=arg_type,
            help=help_text,
            default=default_value,
            required=required,
        )

    return parser


# Self styled message
def format_msg(target: str, title: str, desc: str):
    ss = io.StringIO()
    ss.write(f"[{title.upper()}]")
    ss.write(f" ---{desc.replace(' ','-')}---" if desc else "")
    ss.write(f" {target}" if target else "")
    return ss.getvalue()


speaker_dict = {
    "001": "RK Gorani",
    "002": "Maibam Dwijamani",
    "003": "Ngangbam Nganthoi",
    "004": "Ngangom Kiran",
    "005": "Nayeni Devi",
    "006": "Wahengbam Rajesh",
    "007": "Nolini Devi",
    "008": "Wahengbam Washington",
    "009": "Kshetrimayum Chitrabhanu",
    "011": "Ningthoukhongjam Suni",
    "013": "Moirangthem Ibeyaibi",
}
month_dict = {
    "01": "Jan",
    "02": "Feb",
    "03": "Mar",
    "04": "Apr",
    "05": "May",
    "06": "Jun",
    "07": "Jul",
    "08": "Aug",
    "09": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec",
}
time_dict = {"00": "0730", "01": "1200", "02": "1930"}
year_dict = {"20": "2020", "21": "2021"}
