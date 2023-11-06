from pathlib import Path
from typing import Dict, List
from .utils.file import read_file
from .utils.utterance import dict_to_str, utt_id


class Segmentation:
    def __str__(self) -> str:
        return "Segmentation"

    # Public methods
    def segment(self, file_path: Path) -> str:
        # Step 1: Build Utterance Dictionary with utterances and corresponding ids
        utterances = self.__init_utts(
            input_data=read_file(file_path=file_path),
            file_path=file_path,
        )

        # Returns final content
        return dict_to_str(utterances)

    # Private methods
    def __init_utts(self, input_data: str, file_path: Path) -> Dict:
        return {
            utt_id(file_name=file_path.name.split(".")[0], idx=idx): utt
            for idx, utt in enumerate(self.__get_utt_rows(content=input_data))
        }

    def __get_utt_rows(self, content: str) -> List[str]:
        self.cheikhei = "ú"
        self.delimiter = self.cheikhei
        self.whitespaces = [
            "\u200b",
            "\u200c",
            "\u200d",
            "\u200e",
            "\u200f",
            "\t",
            "\r",
            "\u0020",
            "\u0009",
            "\u000a",
        ]
        utts = []
        for utt in content.split(self.delimiter):
            if utt.strip() not in self.whitespaces:
                utts.append(utt.strip())
        cleaned_utts = [utt.strip() for utt in utts]
        return cleaned_utts
