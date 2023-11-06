from pathlib import Path
from .utils.file import read_file
from .utils.utterance import (
    str_to_dict,
    dict_to_str,
)


class MMTransliteration:
    def __init__(self) -> None:
        self.__init_vars()

    def __str__(self) -> str:
        return "Transliteration"

    # Initializations
    def __init_vars(self):
        self.virama = "\u09cd"

    # Public methods
    def transliterate_script(self, file_path: Path) -> str:
        return self.transliterate(read_file(file_path=file_path))

    def transliterate_utterances(self, file_path: Path) -> str:
        utterances_dict = str_to_dict(read_file(file_path=file_path))
        return dict_to_str(
            {utt_id: self.transliterate(utt) for utt_id, utt in utterances_dict.items()}
        )

    def transliterate(self, content: str) -> str:
        # Returns final data
        return content
