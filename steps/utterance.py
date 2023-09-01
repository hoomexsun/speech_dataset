from pathlib import Path
from typing import Dict, List
from config.project import Project
from utils.file import fbuild_id, fread
from utils.text import clean_s550_data, utt_dict_to_content


class Utterance(Project):
    def __init__(self) -> None:
        super().__init__("Utterance")
        self.__init_vars()

    # Initializations
    def __init_vars(self):
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

    # Public methods
    def utterance(self, file_path: Path) -> str:
        # Step 1: Build Utterance Dictionary with utterances and corresponding ids
        utterances = self.__init_utts(
            input_data=fread(file_path=file_path),
            file_path=file_path,
        )

        # Step 2: Build Utterance File from Dictionary
        content = utt_dict_to_content(utterances)

        # Returns final content
        return content

    # Private methods
    def __init_utts(self, input_data: str, file_path: Path) -> Dict:
        return {
            fbuild_id(file_path=file_path, idx=idx): utt
            for idx, utt in enumerate(self.__get_utt_rows(content=input_data))
        }

    def __get_utt_rows(self, content: str) -> List[str]:
        utts = []
        for utt in content.split(self.delimiter):
            if utt.strip() not in self.whitespaces:
                utts.append(utt.strip())
        cleaned_utts = [clean_s550_data(utt) for utt in utts if utt.strip()]
        return cleaned_utts
