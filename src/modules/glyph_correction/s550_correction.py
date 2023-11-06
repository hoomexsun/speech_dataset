from pathlib import Path
from typing import List, Tuple
from .assets import Resource
from .utils.file import read_file
from .utils.text import (
    fix_mistypes,
    remove_chars,
    replace_chars,
)
from .utils.utterance import (
    str_to_dict,
    dict_to_str,
)


class GlyphCorrection:
    def __init__(self) -> None:
        self.res = Resource()

    def __str__(self) -> str:
        return "S-550 Glyph Correction"

    # Public methods
    def correct_script(self, file_path: Path) -> str:
        return self.correct(read_file(file_path=file_path))

    def correct_utterances(self, file_path: Path) -> str:
        utterances_dict = str_to_dict(read_file(file_path))
        return dict_to_str(
            {utt_id: self.correct(utt) for utt_id, utt in utterances_dict.items()}
        )

    def correct(self, text: str) -> str:
        # Step 0: Adjusting s550 characters
        text = self.__adjust(text)

        # Step 1: Mapping Bengali Alphabet
        text = self.__map_unicode(text)

        # Step 2: Remove insignificant characters
        text = self.__remove_insignificant_chars(text)

        # Step 3: Fix suffix position of r
        text = self.__fix_suffix_r(text)

        # Step 4: Post mapping r
        text = self.__post_mapping_r(text)

        # Step 5: Fix prefix position of vowels
        text = self.__fix_prefix_v(text)

        # Step 6: Combine vowels
        text = self.__combine_vowels(text)

        # Returns final content
        return text

    # Private methods
    def __adjust(self, text: str) -> str:
        for key, value in self.res.s550_adjust.items():
            text = text.replace(key, value)
        return text

    def __map_unicode(self, text: str) -> str:
        bn_map = self.res.bn_map()
        MAX_KEY_LENGTH = 3
        for key_length in range(MAX_KEY_LENGTH, 0, -1):
            for key, value in bn_map[key_length].items():
                text = text.replace(key, value)
        return self.__fix_double_virama(text)

    def __fix_double_virama(self, text: str) -> str:
        return fix_mistypes(content=text, chars=[self.res.virama])

    def __fix_suffix_r(self, text: str) -> str:
        char_list = []
        for idx, char in enumerate(text):
            if char in self.res.bn_suffix_r:
                if idx > 6:
                    substring, offset = self.__jump(text[idx - 7 : idx + 1][::-1])
                elif idx > 4:
                    substring, offset = self.__jump(text[idx - 5 : idx + 1][::-1])
                elif idx > 2:
                    substring, offset = self.__jump(text[idx - 3 : idx + 1][::-1])
                else:
                    substring, offset = self.__jump(text[idx - 1 : idx + 1][::-1])
                char_list = char_list[: idx - offset] + substring[::-1]
            else:
                char_list.append(char)

        return "".join(char_list)

    def __fix_prefix_v(self, text: str) -> str:
        char_list = []
        skip_index = -1
        for idx, char in enumerate(text):
            if idx == skip_index:
                skip_index = -1
            elif char in self.res.bn_prefix_vowels:
                if idx <= len(text) - 7:
                    substring, offset = self.__jump(text[idx : idx + 8])
                elif idx <= len(text) - 5:
                    substring, offset = self.__jump(text[idx : idx + 6])
                else:
                    substring, offset = self.__jump(text[idx : idx + 4])
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

    def __post_mapping_r(self, text: str) -> str:
        return self.__fix_double_virama(
            replace_chars(content=text, charmap=self.res.bn_suffix_r_replacement)
        )

    def __combine_vowels(self, text: str) -> str:
        return replace_chars(content=text, charmap=self.res.bn_double_vowel_charmap)

    def __remove_insignificant_chars(self, text: str) -> str:
        return remove_chars(content=text, chars=self.res.s550_insignificant_chars)
