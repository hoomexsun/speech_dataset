from src.config.paths import (
    ALPHABET_DIR,
    B2M_FILE,
    CORRECTION_DIR,
    FPOS_FILE,
    MM_ALPHABET_FILE,
    SNB_FILE,
    TRANSLITERATION_DIR,
)
from src.utils.file import fwrite_json
from src.utils.resource_bank import *


def init_correction_resource(res_dir=CORRECTION_DIR):
    s550_single_charmap = {
        **s550_single_single,
        **s550_prefix,
        **s550_suffix,
        **s550_single_double_v,
        **s550_single_double,
        **s550_single_triple,
        **s550_single_xtra,
    }

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

    write_json_data(chars_to_replace, res_dir / SNB_FILE)
    write_json_data(position_to_fix, res_dir / FPOS_FILE)


def init_transliteration_resource(res_dir=TRANSLITERATION_DIR):
    bn_single_charmap = {
        **bn_c_to_mm_c,
        **bn_v_to_mm_v_begin,
        **bn_v_to_mm_v_mid,
        **bn_num_to_mm_num,
        **bn_punctuation,
    }

    mm_lonsum_to_mapum = {value: key for (key, value) in mm_mapum_to_lonsum.items()}

    bn_to_mm_charmap = {
        "bn_single_charmap": bn_single_charmap,
        "bn_viramma_mm_apun": bn_viramma_mm_apun,
        "bn_viramma_mm_coda": bn_viramma_mm_coda,
        "mm_mapum_to_lonsum": mm_mapum_to_lonsum,
        "mm_lonsum_to_mapum": mm_lonsum_to_mapum,
        "mm_e_lonsum_coda": mm_e_lonsum_coda,
    }

    write_json_data(bn_to_mm_charmap, res_dir / B2M_FILE)


def init_alphabet_resource(res_dir=ALPHABET_DIR):
    mm_chars = mm_mapum + mm_lonsum + mm_cheitap + mm_cheising + mm_khudam

    mm_charmap = {
        "mm_chars": mm_chars,
        "mm_mapum": mm_mapum,
        "mm_lonsum": mm_lonsum,
        "mm_cheitap": mm_cheitap,
        "mm_cheising": mm_cheising,
        "mm_khudam": mm_khudam,
    }

    write_json_data(mm_charmap, res_dir / MM_ALPHABET_FILE)


def write_json_data(data, file_path):
    fwrite_json(data=data, file_path=file_path)


def init_resources():
    init_correction_resource()
    init_transliteration_resource()
    init_alphabet_resource()


if __name__ == "__main__":
    init_resources()
