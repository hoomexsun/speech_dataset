import argparse
from pathlib import Path
from src.core.transliteration import Transliteration
from src.utils import process_directory

# -------------------------------- SCRIPT MODE -------------------------------- #
# TODO: Wordmap part yet to be implemented
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="ransliterates Bengali Unicode to Meetei Mayek Unicode using a rule-based method, supporting transliteration through a wordmap."
    )

    parser.add_argument("input_string", type=str, help="Input string to transliterate.")
    t = Transliteration()
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-f", "--file", action="store_true", help="Input is a file name."
    )
    group.add_argument("-d", "--dir", action="store_true", help="Input is a directory.")
    args = parser.parse_args()

    if args.file:
        t.transliterate_script(file_path=Path(args.input_string))
    elif args.dir:
        directory_path = Path(args.input_string)
        if directory_path.is_dir():
            process_directory(t.transliterate_script, directory_path)
        else:
            print(f"{directory_path} is not a valid directory.")
    else:
        print(t.transliterate(args.input_string))
