from pathlib import Path
from typing import List, Tuple
from config.paths import *
from utils.utils import Project, Utils
from steps.utterance import Utterance


class Correction(Project):
    def __init__(
        self, title: str = "Correction", num_files: int = 0, quiet: bool = True
    ) -> None:
        super().__init__(title, num_files, quiet)
        self.__init_vars()
        self.__init_res()

    # Initializations
    def __init_vars(self):
        self.res_dir = CORRECTION_DIR
        self.virama = "\u09cd"

    def __init_res(self):
        chars_to_replace = Utils.get_dict_from_json(file_path=self.res_dir / SNB_FILE)
        position_to_fix = Utils.get_dict_from_json(file_path=self.res_dir / FPOS_FILE)
        self.s550_single_charmap = chars_to_replace.get("s550_single_charmap", {})
        self.s550_double_charmap = chars_to_replace.get("s550_double_charmap", {})
        self.s550_triple_charmap = chars_to_replace.get("s550_triple_charmap", {})
        self.s550_insignificant_chars = position_to_fix.get(
            "s550_insignificant_chars", []
        )
        self.s550_fix_suffix_char_r = position_to_fix.get("s550_suffix_char_r", [])
        self.bn_fix_prefix_char_v = position_to_fix.get("bn_prefix_char_v", [])
        self.bn_fix_suffix_char_v = position_to_fix.get("bn_suffix_char_v", [])
        self.s550_post_charmap = chars_to_replace.get("s550_post_charmap", {})
        self.bn_double_vowel_charmap = chars_to_replace.get(
            "bn_double_vowel_charmap", {}
        )
        self.bn_fix_error_charmap = chars_to_replace.get("bn_fix_error_charmap", {})

    # Public methods
    def correct_script(self, file_path: Path) -> str:
        return self.correct(Utils.read_encoded_file(file_path=file_path))

    def correct_utterances(
        self, file_path: Path, idx: int = -1, is_utt: bool = False
    ) -> str:
        utterances_dict = Utterance.utt_content_to_dict(
            Utils.read_encoded_file(file_path)
        )
        return Utterance.utt_dict_to_content(
            {utt_id: self.correct(utt) for utt_id, utt in utterances_dict.items()}
        )

    def correct(self, content: str) -> str:
        # Step 1: Remove insignificant characters
        content = self.__remove_insignificant_chars(content)

        # Step 2: Mapping to Unicode
        content = self.__map_unicode(content)

        # Step 3: Fix double virama
        content = self.__fix_double_virama(content)

        # Step 4: Fix suffix position of r
        content = self.__fix_suffix_r(content)

        # Step 5: Post mapping r
        content = self.__post_mapping_r(content)

        # Step 6: Fix prefix position of vowels
        content = self.__fix_prefix_v(content)

        # Step 7: Combine vowels
        content = self.__combine_vowels(content)

        # Step 8: Fix all the small errors and mistypes
        content = self.__fix_errors_and_mistypes(content)

        # Returns final content
        return content

    # Extra Public methods

    # Private methods
    def __remove_insignificant_chars(self, data: str) -> str:
        return Utils.remove_chars(content=data, chars=self.s550_insignificant_chars)

    def __map_unicode(self, data: str) -> str:
        mapped_data = []
        i = 0
        while i < len(data):
            triple_char = data[i : i + 3]
            double_char = data[i : i + 2]
            if triple_char in self.s550_triple_charmap:
                mapped_data.append(self.s550_triple_charmap[triple_char])
                i += 3
            elif double_char in self.s550_double_charmap:
                mapped_data.append(self.s550_double_charmap[double_char])
                i += 2
            else:
                mapped_data.append(self.s550_single_charmap.get(data[i], data[i]))
                i += 1
        return "".join(mapped_data)

    def __fix_double_virama(self, data: str) -> str:
        return Utils.fix_mistypes(content=data, chars=[self.virama])

    def __fix_suffix_r(self, data: str) -> str:
        fixed_data = []
        for i in range(len(data)):
            if data[i] in self.s550_fix_suffix_char_r:
                if i > 7:
                    previous_letters = data[i - 7 : i]
                    (
                        fixed_string_as_list,
                        returned_index,
                        err,
                    ) = self.__find_and_fix_position(
                        letter=data[i], remaining_letters=list(previous_letters[::-1])
                    )
                elif i > 5:
                    previous_letters = data[i - 5 : i]
                    (
                        fixed_string_as_list,
                        returned_index,
                        err,
                    ) = self.__find_and_fix_position(
                        letter=data[i], remaining_letters=list(previous_letters[::-1])
                    )
                elif i > 3:
                    previous_letters = data[i - 3 : i]
                    (
                        fixed_string_as_list,
                        returned_index,
                        err,
                    ) = self.__find_and_fix_position(
                        letter=data[i], remaining_letters=list(previous_letters[::-1])
                    )
                else:
                    previous_letters = data[i - 1 : i]
                    (
                        fixed_string_as_list,
                        returned_index,
                        err,
                    ) = self.__find_and_fix_position(
                        letter=data[i], remaining_letters=list(previous_letters[::-1])
                    )
                if err:
                    self.display(
                        desc="Incorrect letters at the start of file", target="FIX"
                    )
                fixed_data = (
                    fixed_data[: i - returned_index] + fixed_string_as_list[::-1]
                )
            else:
                fixed_data.append(data[i])

        return "".join(fixed_data)

    def __post_mapping_r(self, data: str) -> str:
        return Utils.replace_chars(content=data, charmap=self.s550_post_charmap)

    def __fix_prefix_v(self, data: str) -> str:
        fixed_data = []
        skip_index = -1
        for i in range(len(data)):
            if data[i] in self.bn_fix_prefix_char_v:
                if i + 7 <= len(data):
                    next_letters = data[i + 1 : i + 7]
                    (
                        fixed_string_as_list,
                        indices_to_skip,
                        err,
                    ) = self.__find_and_fix_position(
                        letter=data[i], remaining_letters=list(next_letters)
                    )
                elif i + 5 <= len(data):
                    next_letters = data[i + 1 : i + 5]
                    (
                        fixed_string_as_list,
                        indices_to_skip,
                        err,
                    ) = self.__find_and_fix_position(
                        letter=data[i], remaining_letters=list(next_letters)
                    )
                else:
                    next_letters = data[i + 1 : i + 3]
                    (
                        fixed_string_as_list,
                        indices_to_skip,
                        err,
                    ) = self.__find_and_fix_position(
                        letter=data[i], remaining_letters=list(next_letters)
                    )
                if err:
                    self.display(
                        desc="Incorrect letters at the end of file", target="FIX"
                    )
                fixed_data += fixed_string_as_list
                skip_index = i + indices_to_skip
            elif i == skip_index:
                skip_index = -1
            elif i > skip_index:
                fixed_data.append(data[i])

        return "".join(fixed_data)

    def __combine_vowels(self, data: str) -> str:
        return Utils.replace_chars(content=data, charmap=self.bn_double_vowel_charmap)

    def __fix_errors_and_mistypes(self, data: str) -> str:
        data = Utils.replace_chars(content=data, charmap=self.bn_fix_error_charmap)
        return Utils.fix_mistypes(
            content=data, chars=self.bn_fix_prefix_char_v + self.bn_fix_suffix_char_v
        )

    def __find_and_fix_position(
        self, letter: str, remaining_letters: List[str]
    ) -> Tuple[List, int, bool]:
        index_to_put = 0
        if len(remaining_letters) > 1 and remaining_letters[1] == self.virama:
            index_to_put += 2
            if len(remaining_letters) > 3 and remaining_letters[3] == self.virama:
                index_to_put += 2
                if len(remaining_letters) > 5 and remaining_letters[5] == self.virama:
                    index_to_put += 2

        if index_to_put >= len(remaining_letters):
            return list(letter) + remaining_letters, 1, True

        fixed_string_as_list = list(remaining_letters[0])
        for i in range(index_to_put):
            remaining_letters[i] = remaining_letters[i + 1]
        remaining_letters[index_to_put] = letter
        fixed_string_as_list += remaining_letters
        next_index_after_letter = index_to_put + 1

        return (
            fixed_string_as_list[: next_index_after_letter + 1],
            next_index_after_letter,
            False,
        )
