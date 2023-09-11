from pathlib import Path
import re
from src.utils.project import Project
from src.utils.file import fget_rtf_text, fread


# TODO: Add tokenization
class Preprocessing(Project):
    def __init__(self) -> None:
        super().__init__("Preprocessing")
        self.__init_strings()

    # Initializations
    def __init_strings(self):
        self.signature_tune = "[ÎKì>W¡¹ iå¡¸>"
        # self.newspaper_headline = "[>l¡ü\\ ìšš¹ ëÒƒºàÒü"
        self.newspaper_headline = "[>l¡ü\\"
        self.marker = "@"
        self.sound_bytes = "Îàl¡ü–ƒ ¤ààÒüi¡"
        self.cheikhei = "ú"
        self.maruoiba_pao = "³¹ç¡*Òü¤à šàl¡ü"

    # Public methods
    def preprocess_file(self, file_path: Path, idx: int = -1) -> str:
        if file_path.suffix == ".rtf":
            return self.preprocess(fget_rtf_text(file_path=file_path))
        elif file_path.suffix == ".txt":
            return self.preprocess(fread(file_path=file_path))
        else:
            return "Unsupported file type"

    def preprocess(self, news_string: str) -> str:
        # Step 1: Remove everything before the first signature tune (inaudible)
        news_string = self.remove_before_substring(news_string, self.signature_tune)

        # Step 2: Remove everything after Newspaper headline part if it exists (different speaker)
        news_string = self.remove_after_last_substring(
            news_string, self.newspaper_headline
        )

        # Step 3: Remove every word before @ in the same line as it is markers (inaudible)
        news_string = self.remove_words_before_character(news_string, self.marker)

        # Step 4: Remove all signature tunes line (inaudible)
        news_string = self.remove_all_occurrences(news_string, self.signature_tune)

        # Step 5: Remove all sound bytes line (inaudible)
        news_string = self.replace_all_occurrences(news_string, self.sound_bytes, "\n")

        # Step 6: Remove numberings (inaudible)
        news_string = self.remove_number_before_substring(news_string, ")")

        # Step 7: Replace punctuations, new lines, and tab spaces with empty space
        punctuations = ["\n", "\t", ".", "-", "(", ")", "‘", "’"]
        for punctuation in punctuations:
            news_string = news_string.replace(punctuation, " ")

        # Step 8: Replace multiple spaces into one single space
        news_string = re.sub(r"\s+", " ", news_string).strip()

        # Step 9: Divide single string to multiple lines based on cheikhei
        news_string = (
            news_string.replace(
                f"{self.maruoiba_pao}", f"{self.maruoiba_pao} {self.cheikhei}", 1
            )
            .replace(f"{self.cheikhei}", f"{self.cheikhei}\n")
            .replace("\n ", "\n")
        )

        return news_string

    # Private methods
    @staticmethod
    def remove_before_substring(input_string, substring):
        index = input_string.find(substring)
        if index != -1:
            return input_string[index + len(substring) :]
        else:
            return input_string

    @staticmethod
    def remove_after_last_substring(input_string, substring):
        index = input_string.rfind(substring)
        if index != -1:
            return input_string[:index]
        else:
            return input_string

    @staticmethod
    def remove_words_before_character(input_string, character):
        lines = input_string.split("\n")
        result_lines = [
            line.split(character, 1)[-1].lstrip() if character in line else line
            for line in lines
        ]

        return "\n".join(result_lines)

    @staticmethod
    def remove_all_occurrences(input_string, substring):
        modified_string = input_string.replace(substring, "")
        return modified_string

    @staticmethod
    def replace_all_occurrences(input_string, substring, replacement):
        modified_string = input_string.replace(substring, replacement)
        return modified_string

    @staticmethod
    def remove_number_before_substring(input_string, character):
        lines = input_string.split("\n")
        result_lines = []

        for line in lines:
            index = line.find(character)
            if index != -1 and Preprocessing.check_for_numbers(line[:index]):
                updated_line = line.split(character, 1)[-1].lstrip()
            else:
                updated_line = line
            result_lines.append(updated_line)

        return "\n".join(result_lines)

    @staticmethod
    def check_for_numbers(substring) -> bool:
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(len(substring)):
            if substring[i] not in numbers:
                return False
        return True
