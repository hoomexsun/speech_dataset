from pathlib import Path
from typing import List, Tuple
from src.core.res import Resource
from src.utils.file import fread
from src.utils.project import Project
from src.utils.text import (
    fix_mistypes,
    remove_chars,
    replace_chars,
    utt_content_to_dict,
    utt_dict_to_content,
)


class Correction(Project):
    def __init__(self) -> None:
        super().__init__("Correction")
        self.res = Resource()

    # Public methods
    def correct_script(self, file_path: Path) -> str:
        return self.correct(fread(file_path=file_path))

    def correct_utterances(self, file_path: Path) -> str:
        utterances_dict = utt_content_to_dict(fread(file_path))
        return utt_dict_to_content(
            {utt_id: self.correct(utt) for utt_id, utt in utterances_dict.items()}
        )

    def correct(self, content: str) -> str:
        # Step 0: Adjusting s550 characters
        content = self.__adjust(content)

        # Step 1: Mapping Bengali Alphabet
        content = self.__map_unicode(content)

        # Step 2: Remove insignificant characters
        content = self.__remove_insignificant_chars(content)

        # Step 3: Fix suffix position of r
        content = self.__fix_suffix_r(content)

        # Step 4: Post mapping r
        content = self.__post_mapping_r(content)

        # Step 5: Fix prefix position of vowels
        content = self.__fix_prefix_v(content)

        # Step 6: Combine vowels
        content = self.__combine_vowels(content)

        # Returns final content
        return content

    # Private methods
    def __adjust(self, data: str) -> str:
        for key, value in self.res.s550_adjust.items():
            data = data.replace(key, value)
        return data

    def __map_unicode(self, data: str) -> str:
        bn_map = self.res.bn_map()
        MAX_KEY_LENGTH = 3
        for key_length in range(MAX_KEY_LENGTH, 0, -1):
            for key, value in bn_map[key_length].items():
                data = data.replace(key, value)
        return self.__fix_double_virama(data)

    def __fix_double_virama(self, data: str) -> str:
        return fix_mistypes(content=data, chars=[self.res.virama])

    def __fix_suffix_r(self, data: str) -> str:
        char_list = []
        for idx, char in enumerate(data):
            if char in self.res.bn_suffix_r:
                if idx > 6:
                    substring, offset = self.__jump(data[idx - 7 : idx + 1][::-1])
                elif idx > 4:
                    substring, offset = self.__jump(data[idx - 5 : idx + 1][::-1])
                elif idx > 2:
                    substring, offset = self.__jump(data[idx - 3 : idx + 1][::-1])
                else:
                    substring, offset = self.__jump(data[idx - 1 : idx + 1][::-1])
                char_list = char_list[: idx - offset] + substring[::-1]
            else:
                char_list.append(char)

        return "".join(char_list)

    def __fix_prefix_v(self, data: str) -> str:
        char_list = []
        skip_index = -1
        for idx, char in enumerate(data):
            if idx == skip_index:
                skip_index = -1
            elif char in self.res.bn_prefix_vowels:
                if idx <= len(data) - 7:
                    substring, offset = self.__jump(data[idx : idx + 8])
                elif idx <= len(data) - 5:
                    substring, offset = self.__jump(data[idx : idx + 6])
                else:
                    substring, offset = self.__jump(data[idx : idx + 4])
                char_list += substring
                skip_index = idx + offset
            elif idx > skip_index:
                char_list.append(char)

        return "".join(char_list)

    def __jump(self, chars: str) -> Tuple[List[str], int]:
        char, *right = chars
        idx = 0
        while idx < len(right) - 1 and right[idx + 1] == self.res.virama:
            idx += 2
        if idx >= len(right):
            return list(chars), 1
        return (right[: idx + 1] + [char], idx + 1)

    def __post_mapping_r(self, data: str) -> str:
        return self.__fix_double_virama(
            replace_chars(content=data, charmap=self.res.bn_suffix_r_replacement)
        )

    def __combine_vowels(self, data: str) -> str:
        return replace_chars(content=data, charmap=self.res.bn_double_vowel_charmap)

    def __remove_insignificant_chars(self, data: str) -> str:
        return remove_chars(content=data, chars=self.res.s550_insignificant_chars)
