import io
from pathlib import Path
from typing import Dict, List, Union
from utils.file import write_markdown_file

# TODO: Doesn't look good for clusters


class MarkdownBuilderUtils:
    MAX_HEADER_LEVEL = 6

    @staticmethod
    def build_markdown_file(
        d: Dict[str, Union[Dict, List, str, int, float]], file_name: str
    ):
        content = MarkdownBuilderUtils.build_markdown_content(d=d)
        MarkdownBuilderUtils.save_markdown_file(content=content, file_name=file_name)

    @staticmethod
    def build_markdown_content(d: Dict[str, Union[Dict, List, str, int, float]]) -> str:
        string_io = io.StringIO()
        MarkdownBuilderUtils.section(d=d, string_io=string_io)
        return string_io.getvalue()

    @staticmethod
    def section(d: Dict, string_io: io.StringIO, current_level: int = 0) -> None:
        for key, value in d.items():
            string_io.write(
                MarkdownBuilderUtils.format_header(
                    line=str(key), level=current_level + 1
                )
            )
            if isinstance(value, dict):
                MarkdownBuilderUtils.section(value, string_io, current_level + 1)
            elif isinstance(value, list):
                string_io.write(
                    "\n".join([f"{i+1}. {val}" for i, val in enumerate(value)])
                )
                string_io.write("\n\n")
            elif (
                isinstance(value, str)
                or isinstance(value, int)
                or isinstance(value, float)
            ):
                string_io.write(f"{value}\n\n")

    @staticmethod
    def format_header(line: str, level: int) -> str:
        line = line.replace("\n", " ")
        level = min(level, MarkdownBuilderUtils.MAX_HEADER_LEVEL)
        header_prefix = "#" * level
        return f"{header_prefix} {line}\n\n"

    @staticmethod
    def save_markdown_file(content: str, file_name: str) -> None:
        output_path = Path("output/markdowns") / file_name
        write_markdown_file(content=content, file_path=output_path)
