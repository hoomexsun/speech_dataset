from config.project import Project
from config.paths import *
from utils.file import fwrite_json
from utils.resource_bank import *


class Correction_resource(Project):
    def __init__(self, res_dir: Path = CORRECTION_DIR) -> None:
        super().__init__("Correction resource")
        self.res_dir = res_dir
        self.__init_res()

    def __init_res(self):
        s550_single_charmap = {
            **s550_single_single,
            **s550_prefix,
            **s550_suffix,
            **s550_single_double_v,
            **s550_single_double,
            **s550_single_triple,
            **s550_single_xtra,
        }  # dictionary unpacking
        chars_to_replace = {
            "s550_single_charmap": s550_single_charmap,
            "s550_double_charmap": s550_double_charmap,
            "s550_triple_charmap": s550_triple_charmap,
            "s550_post_charmap": s550_post_charmap,
            "bn_double_vowel_charmap": bn_double_vowel_charmap,
            "bn_fix_error_charmap": bn_fix_error_charmap,
        }
        position_to_fix = {
            "s550_insignificant_chars": s550_invisible_char,
            "s550_suffix_char_r": s550_suffix_char_r,
            "bn_prefix_char_v": bn_prefix_char_v,
            "bn_suffix_char_v": bn_suffix_char_v,
        }

        fwrite_json(data=chars_to_replace, file_path=self.res_dir / SNB_FILE)
        fwrite_json(data=position_to_fix, file_path=self.res_dir / FPOS_FILE)


class Transliteration_resource(Project):
    def __init__(self, res_dir: Path = TRANSLITERATION_DIR) -> None:
        super().__init__("Transliteration resource")
        self.res_dir = res_dir
        self.__init_res()

    def __init_res(self):
        bn_single_charmap = {
            **bn_c_to_mm_c,
            **bn_v_to_mm_v_begin,
            **bn_v_to_mm_v_mid,
            **bn_num_to_mm_num,
            **bn_punctuation,
        }  # dictionary unpacking
        mm_lonsum_to_mapum = {value: key for (key, value) in mm_mapum_to_lonsum.items()}
        bn_to_mm_charmap = {
            "bn_single_charmap": bn_single_charmap,
            "bn_viramma_mm_apun": bn_viramma_mm_apun,
            "bn_viramma_mm_coda": bn_viramma_mm_coda,
            "mm_mapum_to_lonsum": mm_mapum_to_lonsum,
            "mm_lonsum_to_mapum": mm_lonsum_to_mapum,
            "mm_e_lonsum_coda": mm_e_lonsum_coda,
        }

        fwrite_json(data=bn_to_mm_charmap, file_path=self.res_dir / B2M_FILE)


class Alphabet_resource(Project):
    def __init__(self, res_dir: Path = ALPHABET_DIR) -> None:
        super().__init__("Alphabet resource")
        self.__init_res()

    def __init_res(self):
        mm_chars = mm_mapum + mm_lonsum + mm_cheitap + mm_cheising + mm_khudam
        mm_charmap = {
            "mm_chars": mm_chars,
            "mm_mapum": mm_mapum,
            "mm_lonsum": mm_lonsum,
            "mm_cheitap": mm_cheitap,
            "mm_cheising": mm_cheising,
            "mm_khudam": mm_khudam,
        }
        fwrite_json(data=mm_charmap, file_path=MM_ALPHABET_FILE)


def init_resources():
    cr = Correction_resource()
    tr = Transliteration_resource()
    ar = Alphabet_resource()


if __name__ == "__main__":
    init_resources()
