import argparse
from config.paths import *
from steps.utterance import Utterance
from typing import List
from utils.utils import Project, Utils


class Transliteration(Project):
    def __init__(
        self, title: str = "Transliteration", num_files: int = 0, quiet: bool = True
    ) -> None:
        super().__init__(title, num_files, quiet)
        self.__init_vars()
        self.__init_res()

    # Initializations
    def __init_vars(self):
        self.res_dir = TRANSLITERATION_DIR
        self.virama = "\u09cd"

    def __init_res(self):
        b2m_charmap = Utils.get_dict_from_json(file_path=self.res_dir / B2M_FILE)
        mm_charmap = Utils.get_dict_from_json(file_path=MM_ALPHABET_FILE)
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
        return self.transliterate(Utils.read_encoded_file(file_path=file_path))

    def transliterate_utterances(self, file_path: Path) -> str:
        utterances_dict = Utterance.utt_content_to_dict(
            Utils.read_encoded_file(file_path=file_path)
        )
        return Utterance.utt_dict_to_content(
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

        # Returns final data
        return content

    # Extra Public methods
    def word_map(self, input_data: str, wmap_file: Path = WORDMAP_T_FILE) -> str:
        wmap_dict = Utils.get_dict_from_json(wmap_file)
        output = [
            wmap_dict.get(word, self.transliterate(content=word))
            for word in input_data.split()
        ]
        return "".join(output)

    # Private methods
    def pre_mapping(self, data: str) -> str:
        return Utils.replace_chars(content=data, charmap=self.bn_single_charmap)

    def fix_apun(self, data: str) -> str:
        return Utils.replace_two_chars(content=data, charmap=self.bn_viramma_mm_apun)

    def fix_coda_viramma(self, data: str) -> str:
        return Utils.replace_two_chars(content=data, charmap=self.bn_viramma_mm_coda)

    def fix_coda_lonsum(self, data: str) -> str:
        return Utils.replace_two_chars(content=data, charmap=self.mm_e_lonsum_coda)

    def fix_lonsum_from_mapum_pair(self, data: str) -> str:
        output_data = list(data)
        for i in range(len(data) - 1):
            char, next_char = data[i], data[i + 1]
            if char in self.mm_cheitap:
                output_data[i + 1] = self.mm_mapum_to_lonsum.get(next_char, next_char)

        return "".join(output_data)

    def find_and_fix_lonsum(self, data: str) -> str:
        output_data = list(data)
        i = 0
        while i < len(data) - 1:
            char, next_char = data[i], data[i + 1]
            if char in self.mm_mapum and next_char in self.mm_mapum:
                if char not in ["\uabd1"]:
                    output_data[i + 1] = self.mm_mapum_to_lonsum.get(
                        next_char, next_char
                    )
                i += 1
            elif char in self.mm_lonsum and next_char in self.mm_lonsum:
                output_data[
                    i
                ] = f"{output_data[i]}{self.mm_lonsum_to_mapum.get(char, char)}"
                i += 1
            i += 1
        return "".join(output_data)


# -------------------------------- SCRIPT MODE -------------------------------- #
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Transliteration of bengali unicode text to correct meetei mayek unicode text using rule based method.')
#     group = parser.add_mutually_exclusive_group()
#     parser.add_argument('input', type=str, help="enter input string.")
#     group.add_argument('-f', '--file', action='store_true', help="input is a file name.")
#     group.add_argument('-d', '--dir', action='store_true', help='input is a directory.')
#     args = parser.parse_args()

#     t = Transliteration()
#     if args.file:
#         t.run_file(file=Path(args.input))
#     elif args.dir:
#         t.run_files(dir=Path(args.input))
#     else:
#         print(t.transliterate(args.input))
