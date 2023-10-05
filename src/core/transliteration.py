from pathlib import Path
from src.config.paths import (
    B2M_FILE,
    MM_ALPHABET_FILE,
    TRANSLITERATION_DIR,
    WORDMAP_T_FILE,
)
from src.utils.file import fget_dict, fread
from src.utils.text import (
    replace_chars,
    replace_two_chars,
    utt_content_to_dict,
    utt_dict_to_content,
)
from src.utils.project import Project


class Transliteration(Project):
    def __init__(self) -> None:
        super().__init__("Transliteration")
        self.__init_vars()
        self.__init_res()

    # Initializations
    def __init_vars(self):
        self.res_dir = TRANSLITERATION_DIR
        self.virama = "\u09cd"

    def __init_res(self):
        b2m_charmap = fget_dict(file_path=self.res_dir / Path(B2M_FILE))
        mm_charmap = fget_dict(file_path=MM_ALPHABET_FILE)
        self.bn_single_charmap = b2m_charmap.get("bn_single_charmap", {})
        self.bn_viramma_mm_apun = b2m_charmap.get("bn_viramma_mm_apun", {})
        self.bn_viramma_mm_coda = b2m_charmap.get("bn_viramma_mm_coda", {})
        self.mm_e_lonsum_coda = b2m_charmap.get("mm_e_lonsum_coda", {})
        self.mm_mapum_to_lonsum = b2m_charmap.get("mm_mapum_to_lonsum", {})
        self.mm_lonsum_to_mapum = b2m_charmap.get("mm_lonsum_to_mapum", {})
        self.mm_chars = mm_charmap.get("mm_chars", [])
        self.mm_mapum = mm_charmap.get("mm_mapum", [])
        self.mm_lonsum = mm_charmap.get("mm_lonsum", [])
        self.mm_cheitap = mm_charmap.get("mm_cheitap", [])
        self.mm_cheising = mm_charmap.get("mm_cheising", [])
        self.mm_khudam = mm_charmap.get("mm_khudam", [])

    # Public methods
    def transliterate_script(self, file_path: Path) -> str:
        return self.transliterate(fread(file_path=file_path))

    def transliterate_utterances(self, file_path: Path) -> str:
        utterances_dict = utt_content_to_dict(fread(file_path=file_path))
        return utt_dict_to_content(
            {utt_id: self.transliterate(utt) for utt_id, utt in utterances_dict.items()}
        )

    def transliterate(self, content: str) -> str:
        # Step 1: Single letter except viramma
        content = self.pre_mapping(content)

        # Step 2: Fixing apun near r and y
        content = self.fix_apun(content)

        # Step 3: Fixing coda
        content = self.fix_coda_viramma(content)

        # Step 4: Fixing coda
        content = self.fix_coda_lonsum(content)

        # Step 5: Generating lonsum from mapum using cheitap
        content = self.fix_lonsum_from_mapum_pair(content)

        # Step 6: Generate an extra char and find probable lonsum characters
        content = self.find_and_fix_lonsum(content)

        # Step 7: Generate an extra char and find probable lonsum characters
        content = self.find_and_fix_lonsum2(content)

        # Returns final data
        return content

    # Extra Public methods
    def word_map(self, input_data: str, wmap_file: Path = WORDMAP_T_FILE) -> str:
        wmap_dict = fget_dict(wmap_file)
        output = [
            wmap_dict.get(word, self.transliterate(content=word))
            for word in input_data.split()
        ]
        return "".join(output)

    # Private methods
    def pre_mapping(self, data: str) -> str:
        return replace_chars(content=data, charmap=self.bn_single_charmap)

    def fix_apun(self, data: str) -> str:
        return replace_two_chars(content=data, charmap=self.bn_viramma_mm_apun)

    def fix_coda_viramma(self, data: str) -> str:
        return replace_two_chars(content=data, charmap=self.bn_viramma_mm_coda)

    def fix_coda_lonsum(self, data: str) -> str:
        return replace_two_chars(content=data, charmap=self.mm_e_lonsum_coda)

    def fix_lonsum_from_mapum_pair(self, data: str) -> str:
        output_data = list(data)
        for i, char in enumerate(data):
            if char in self.mm_cheitap and i < len(data) - 1:
                output_data[i + 1] = self.mm_mapum_to_lonsum.get(
                    data[i + 1], data[i + 1]
                )
        return "".join(output_data)

    def find_and_fix_lonsum(self, data: str) -> str:
        output_data = list(data)
        for i, char in enumerate(data):
            if (
                char in self.mm_mapum
                and char not in ["\uabd1"]
                and i < len(data) - 1
                and data[i + 1] in self.mm_mapum
            ):
                output_data[i + 1] = self.mm_mapum_to_lonsum.get(
                    data[i + 1], data[i + 1]
                )
        return "".join(output_data)

    def find_and_fix_lonsum2(self, data: str) -> str:
        output_data = list(data)
        for i, char in enumerate(data):
            if (
                char in self.mm_lonsum
                and i < len(data) - 1
                and data[i + 1] in self.mm_lonsum
            ):
                output_data[i] = f"{char}{self.mm_lonsum_to_mapum.get(char, char)}"
        return "".join(output_data)


### NEW

from typing import Any


VOWELS = "aeiou"


class TU:
    def __init__(self, input_str: str) -> None:
        self.input_str = input_str
        self.type = "ws" if self.is_whitespace(input_str) else "sy"
        if self.type == "sy":
            self.syllabify()
            self.typify()

    def is_whitespace(self, inp: str) -> bool:
        return inp in (" ", "\n")

    def syllabify(self) -> None:
        vowel_indices = [i for i, char in enumerate(self.input_str) if char in VOWELS]

        if not vowel_indices:
            self.syllable = ("", "", self.input_str)
        else:
            first_vowel_index = vowel_indices[0]
            vowel_num = len(vowel_indices)
            onset = self.input_str[:first_vowel_index]
            nucleus = self.input_str[first_vowel_index : first_vowel_index + vowel_num]
            coda = self.input_str[first_vowel_index + vowel_num :]
            self.syllable = (onset, nucleus, coda)

    def typify(self) -> None:
        if not self.syllable[0] and not self.syllable[2]:
            self.type = "v"
        elif not self.syllable[0]:
            self.type = "vc"
        elif not self.syllable[2]:
            self.type = "cv"
        else:
            self.type = "cvc"

    def __str__(self) -> str:
        if self.type == "ws":
            return f"Whitespace | {self.input_str}"
        else:
            return f"{self.type} | {self.syllable}"

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(str(self))


if __name__ == "__main__":
    test_cases = ["sfirr", "i", "sfierr", "fierr", "ierr", "err", "ber", " ", "\n"]

    for test_case in test_cases:
        syllable = TU(test_case)
        syllable()
