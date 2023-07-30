import io
from pathlib import Path
from striprtf.striprtf import rtf_to_text
from typing import Dict, List, Tuple
import chardet
import json
import pandas as pd
import csv


class Utils:
    def __init__(
        self,
        title: str = "main",
        num_files: int = 0,
        quiet: bool = False,
    ) -> None:
        """Utility class for various file handling and text processing functions.

        Args:
            title (str, optional): Title for the utility class. Defaults to "main".
            num_files (int, optional): Number of files processed. Defaults to 0.
            quiet (bool, optional): Flag to suppress output. Defaults to False.
        """
        self.title = title
        self.num_files = num_files
        self.quiet = quiet

    # Display Function for use inside the Custom Classes
    def display(self, title: str = "", target: str = "", desc: str = "", idx: int = -1):
        """Display a formatted line with information.

        Args:
            title (str, optional): Title for the line. Defaults to "".
            target (str, optional): Target information for the line. Defaults to "".
            suffix (str, optional): Suffix information for the line. Defaults to "".
            idx (int, optional): Index information for the line. Defaults to -1.
        """
        if not self.quiet:
            self.display_line(
                title=title if title else self.title,
                target=target,
                suffix=desc,
                num_files=self.num_files,
                idx=idx,
            )

    # Display Function for use inside the Custom Classes
    @staticmethod
    def display_line(
        title: str,
        target: str,
        suffix: str,
        num_files: int = 0,
        idx: int = -1,
    ):
        """Display a formatted line with information.

        Args:
            title (str, optional): Title for the line. Defaults to "".
            target (str, optional): Target information for the line. Defaults to "".
            suffix (str, optional): Suffix information for the line. Defaults to "".
            idx (int, optional): Index information for the line. Defaults to -1.
        """
        print(
            Utils.format_line(
                title=title, target=target, suffix=suffix, num_files=num_files, idx=idx
            )
        )

    @staticmethod
    def get_files(dir: Path, extension: str = "txt") -> List[Path]:
        return list(dir.glob(f"*.{extension.lower()}"))

    def set_num_files(self, num_files: int):
        """Set the number of files processed.

        Args:
            num_files (int): Number of files processed.
        """
        self.num_files = num_files

    @staticmethod
    def format_line(
        title: str, target: str, suffix: str, num_files: int = 0, idx: int = -1
    ) -> str:
        """Format a line with information.

        Args:
            title (str): Title for the line.
            target (str): Target information for the line.
            suffix (str): Suffix information for the line.
            idx (int, optional): Index information for the line. Defaults to -1.

        Returns:
            str: Formatted line text.
        """
        ss = io.StringIO()
        ss.write(f"\n[{title.upper()}]")
        if idx != -1:
            ss.write(f" | ({idx+1 if idx != -1 else ''}/{num_files})")
        ss.write(f" {target}" if target else "")
        ss.write(f" ---{suffix.replace(' ','-')}---" if suffix else "")
        return ss.getvalue()

    # File Utility Functions
    @staticmethod
    def get_dict_from_json(file_path: Path) -> Dict:
        """Load data from a JSON file and return it as a dictionary.

        Args:
            file_path (Path): Path to the JSON file.

        Returns:
            Dict: Loaded data as a dictionary.
        """
        json_data = Utils.read_encoded_file(file_path=file_path.with_suffix(".json"))
        return json.loads(json_data)

    @staticmethod
    def get_text_from_rtf(file_path: Path) -> str:
        """Extract plain text from an RTF file.

        Args:
            file_path (Path): Path to the RTF file.

        Returns:
            str: Plain text extracted from the RTF file.
        """
        Utils.display_line(
            title="extract",
            target=file_path.as_posix(),
            suffix="extracting-text-from-rtf",
        )
        with open(file_path, "rb") as rtf_file:
            # Step 1: Read the RTF file as binary data
            rtf_data = rtf_file.read()
            try:
                # Step 2: Check if the RTF data is already UTF-8 encoded
                rtf_text = rtf_data.decode("utf-8")
            except UnicodeDecodeError:
                try:
                    # Step 3: If it's not UTF-8, decode the binary data using the appropriate encoding (e.g., cp1252)
                    rtf_text = rtf_data.decode("cp1252")
                except UnicodeDecodeError:
                    # Step 4: Handle any other decoding errors and replace problematic characters with '?'
                    rtf_text = rtf_data.decode("utf-8", errors="replace")

            # Step 5: Use the rtf_to_text function only if the data is already decoded as a string
            if isinstance(rtf_text, str):
                plain_text = rtf_to_text(rtf_text)
            else:
                raise ValueError("Unable to extract text from the RTF file.")

            # Fix incorrect replacement of characters
            plain_text = plain_text.replace("\x00", "").replace("\xdd", "")

        return plain_text

    @staticmethod
    def write_text_file(content: str, file_path: Path):
        Utils.display_line(
            title="write", target=file_path.as_posix(), suffix="writing-text-file"
        )
        Utils.write_encoded_file(
            content=content, file_path=file_path.with_suffix(".txt")
        )

    @staticmethod
    def write_json_file(data: Dict, file_path: Path, unicode: bool = False) -> None:
        json_data = (
            json.dumps(data) if unicode else json.dumps(data, ensure_ascii=False)
        )
        if unicode:
            file_name = file_path.name + "_utf"
            file_path = file_path.parent / file_name
            Utils.display_line(
                title="write", target=file_path.as_posix(), suffix="writing-json-file"
            )
        else:
            Utils.display_line(
                title="write", target=file_path.as_posix(), suffix="writing-json-file"
            )
        Utils.write_encoded_file(
            content=json_data, file_path=file_path.with_suffix(".json")
        )

    @staticmethod
    def write_csv_file(data: Dict, fieldnames: Tuple, file_path: Path) -> None:
        file_path = file_path.with_suffix(".csv")
        Utils.display_line(
            title="write", target=file_path.as_posix(), suffix="writing-csv-file"
        )
        with open(file_path, mode="w", encoding="utf-8", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for word_bn, word_mm in data.items():
                writer.writerow({fieldnames[0]: word_bn, fieldnames[1]: word_mm})

    # Basic File Utility Functions
    @staticmethod
    def read_encoded_file(file_path: Path) -> str:
        Utils.display_line(
            title="read", target=file_path.as_posix(), suffix="reading-file"
        )
        return file_path.read_text(encoding="utf-8")

    @staticmethod
    def write_encoded_file(content: str, file_path: Path) -> None:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(data=content, encoding="utf-8")

    # Basic Text Utility Functions
    @staticmethod
    def remove_chars(content: str, chars: List[str]) -> str:
        for char in chars:
            content = content.replace(char, "")
        return content

    @staticmethod
    def replace_chars(content: str, charmap: Dict[str, str]) -> str:
        for char, replacement in charmap.items():
            content = content.replace(char, replacement)
        return content

    @staticmethod
    def replace_two_chars(content: str, charmap: Dict[str, str]) -> str:
        if not content:
            return ""
        output_data = []
        i = 0
        while i < len(content) - 1:
            char = content[i : i + 2]
            replacement = charmap.get(char)
            if replacement is not None:
                output_data.append(replacement)
                i += 2
            else:
                output_data.append(char[0])
                i += 1

        return "".join(output_data)

    @staticmethod
    def fix_mistypes(content: str, chars: List[str], num_mistypes: int = 2) -> str:
        for char in chars:
            for num in range(num_mistypes + 1, 2, -1):
                content = content.replace(char * num, char)
        return content

    # Text Utility Functions
    @staticmethod
    def clean_s550_data(content: str) -> str:
        # insignificant_chars = "`~!@#$%^&*()_+=[]}{:;'\",.<>/?"
        insignificant_chars = "()"
        more_chars = ["\u200b", "\u200c", "\u200d", "\u200e", "\u200f", "\xad"]
        space_chars = ".,-\n\t\r\u200c"
        content = content.strip()
        content = Utils.fix_mistypes(
            content=content, chars=list(space_chars), num_mistypes=5
        )
        content = Utils.replace_chars(
            content=content, charmap={char: " " for char in space_chars}
        )
        content = Utils.remove_chars(
            content=content, chars=list(insignificant_chars) + more_chars
        )
        content = Utils.fix_mistypes(content=content, chars=[" "])
        return content

    @staticmethod
    def clean_bn_data(content: str) -> str:
        insignificant_chars = "`~!@#$%^&*()_+=[]}{:;'\",.<>/?"
        more_chars = ["\u200b", "\u200c", "\u200d", "\u200e", "\u200f", "\xad"]
        space_chars = "-\n\t\r\u200c"
        content = content.strip()
        content = Utils.fix_mistypes(
            content=content, chars=list(space_chars), num_mistypes=5
        )
        content = Utils.replace_chars(
            content=content, charmap={char: " " for char in space_chars}
        )
        content = Utils.remove_chars(
            content=content, chars=list(insignificant_chars) + more_chars
        )
        content = Utils.fix_mistypes(content=content, chars=[" "])
        return content

    # Test Functions
    @staticmethod
    def display_unicode(content: str) -> None:
        print(Utils.get_unicode_string(content=content))

    @staticmethod
    def get_unicode_string(content: str) -> str:
        ss = io.StringIO()
        for char in content:
            ss.write("\\u" + format(ord(char), "x").zfill(4))
        return ss.getvalue()

    # Unused Functions
    @staticmethod
    def display_unicode_counts_in_file(file_path: Path):
        data = Utils.read_encoded_file(file_path)
        df = Utils.get_unicode_info_as_df(content=data)
        print(df)

    @staticmethod
    def get_unicode_info_as_df(content: str) -> pd.DataFrame:
        d = {}
        for char in content:
            if char in d:
                d[char]["count"] += 1
            else:
                d[char] = {
                    "char": char,
                    "unicode": Utils.get_unicode_string(char),
                    "count": 1,
                }
        df = pd.DataFrame.from_dict(d, orient="index")
        return df

    # Calculations
    @staticmethod
    def get_pct(num: int, total: int) -> str:
        """Calculate the percentage.

        Args:
            num (int): Numerator value.
            total (int): Total value.

        Returns:
            str: Percentage value formatted as a string with two decimal places.
        """
        return format(100 * num / total, ".2f")
