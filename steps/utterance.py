from itertools import chain
from pathlib import Path
from typing import Dict, List, Tuple
from utils.utils import Project, Utils


class Utterance(Project):
    def __init__(
        self, title: str = "Utterance", num_files: int = 0, quiet: bool = True
    ) -> None:
        super().__init__(title, num_files, quiet)
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
    def utterance_file(self, file_path: Path, idx: int = -1) -> str:
        self.display(title=self.title, target=file_path.as_posix(), idx=idx)
        return self.utterance(
            Utils.read_encoded_file(file_path=file_path), file_path=file_path
        )

    def utterance(self, content: str, file_path: Path) -> str:
        # Step 1: Build Utterance Dictionary with utterances and corresponding ids
        utterances = self.__init_utts(input_data=content, file_path=file_path)

        # Display Number of Utterances
        # Utils.display_line(
        #     title="Utterances",
        #     suffix="Saving Utterances",
        #     target=f"Number of utterances: {len(utterances)}",
        # )

        # Step 2: Build Utterance File from Dictionary
        content = self.utt_dict_to_content(utterances)

        # Returns final content
        return content

    # Extra Public Methods 1
    @staticmethod
    def utt_lists_to_content(utt_ids: List[str], utterances: List[str]) -> str:
        return "".join(f"{utt_id}\t{utt}\n" for utt_id, utt in zip(utt_ids, utterances))

    @staticmethod
    def utt_lists_to_dict(utt_ids: List[str], utterances: List[str]) -> Dict[str, str]:
        return {utt_id: utt for utt_id, utt in zip(utt_ids, utterances)}

    @staticmethod
    def utt_dict_to_content(utterances_dict: Dict[str, str]) -> str:
        return "\n".join(f"{utt_id}\t{utt}" for utt_id, utt in utterances_dict.items())

    @staticmethod
    def utt_content_to_dict(content: str) -> Dict[str, str]:
        if not content:
            return {}
        lines = content.split("\n")
        utt_ids, utterances = [], []
        for line in lines:
            utt_id, *utterance = line.split("\t")
            utt_ids.append(utt_id)
            utterances.extend(utterance)
        return Utterance.utt_lists_to_dict(utt_ids, utterances)

    # Extra Public Methods 2
    @staticmethod
    def get_utt_ids_from_text(file_path: Path) -> List[str]:
        utt_ids, _ = Utterance.split_id_and_utt(file_path=file_path)
        return utt_ids

    @staticmethod
    def get_utterances_from_text(file_path: Path) -> str:
        _, utterances = Utterance.split_id_and_utt(file_path=file_path)
        return "\n".join(utterances)

    @staticmethod
    def split_id_and_utt(file_path: Path) -> Tuple[List, List]:
        temp = Utils.read_encoded_file(file_path=file_path)
        lines = temp.split("\n")
        utt_ids, utterances = [], []
        for line in lines:
            utt_id, *utterance = line.split("\t")
            utt_ids.append(utt_id)
            utterances.extend(utterance)
        return utt_ids, utterances

    # Private methods
    def __init_utts(self, input_data: str, file_path: Path) -> Dict:
        return {
            self.__build_utt_id(file_path=file_path, idx=idx): utt
            for idx, utt in enumerate(self.__get_utt_rows(content=input_data))
        }

    @staticmethod
    def __build_utt_id(file_path: Path, idx: int) -> str:
        utt_id = file_path.name.split(".")[0]
        if idx < 9:  # idx starts from 0
            utt_id = f"{utt_id}00{idx+1}"
        elif idx < 99:
            utt_id = f"{utt_id}0{idx+1}"
        else:
            utt_id = f"{utt_id}{idx+1}"
        return utt_id

    def __get_utt_rows(self, content: str) -> List[str]:
        utts = []
        for utt in content.split(self.delimiter):
            if utt.strip() not in self.whitespaces:
                utts.append(utt.strip())
        cleaned_utts = [Utils.clean_s550_data(utt) for utt in utts if utt.strip()]
        return cleaned_utts
