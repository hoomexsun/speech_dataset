import argparse
from pathlib import Path
from src.core.correction import Correction
from src.utils.project import process_directory


# -------------------------------- SCRIPT MODE -------------------------------- #
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Converts s-550 glyphs into correct Bengali Unicode characters."
    )

    parser.add_argument("input_string", type=str, help="Input string to correct.")
    c = Correction()
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-f", "--file", action="store_true", help="Input is a file name."
    )
    group.add_argument("-d", "--dir", action="store_true", help="Input is a directory.")
    args = parser.parse_args()

    if args.file:
        c.correct_script(file_path=Path(args.input_string))
    elif args.dir:
        directory_path = Path(args.input_string)
        if directory_path.is_dir():
            process_directory(c.correct_script, directory_path)
        else:
            print(f"{directory_path} is not a valid directory.")
    else:
        print(c.correct(args.input_string))
