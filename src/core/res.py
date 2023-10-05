from typing import Dict, List
from src.utils.bn_map import *
from src.utils.mm_map import *


class Resource:
    # Correction Resources
    def bn_map(self) -> Dict[int, Dict[str, str]]:
        bn_dict = {
            **BN_ALPHABET,
            **BN_INCOMPLETE,
            **BN_COMPLETE,
            **BN_VOWEL_LEFT,
            **BN_VOWEL_RIGHT,
            **BN_VOWEL_DOWN,
            **BN_PUNCTUATION,
            **BN_EXTRA,
        }
        grouped_dict = {}
        for key, value in bn_dict.items():
            key_length = len(key)
            if key_length not in grouped_dict:
                grouped_dict[key_length] = {}
            grouped_dict[key_length][key] = value
        return grouped_dict

    @property
    def s550_adjust(self) -> Dict[str, str]:
        return S550_ADJUST

    @property
    def bn_prefix_vowels(self) -> List[str]:
        return list({vowel for vowel in BN_VOWEL_LEFT.values()})

    @property
    def bn_suffix_r(self) -> List[str]:
        return list({r for r in BN_R_RIGHT.keys()})

    @property
    def bn_suffix_r_replacement(self) -> Dict[str, str]:
        return BN_R_RIGHT

    @property
    def virama(self) -> str:
        return "\u09cd"

    @property
    def bn_double_vowel_charmap(self) -> Dict[str, str]:
        return POST_BN_VOWEL_OUTSIDE

    @property
    def en_punctuations(self) -> List[str]:
        return list(EN_PUNCTUATIONS)

    @property
    def s550_insignificant_chars(self) -> List[str]:
        return list(S550_INSIGNIFICANT_CHARS)

    # Transliteration Resources
    @property
    def mm_onset(self) -> Dict[str, str]:
        return MM_ONSET

    @property
    def mm_coda(self) -> Dict[str, str]:
        return MM_CODA

    @property
    def mm_nucleus_begin(self) -> Dict[str, str]:
        return MM_NUCLEUS_BEGIN

    @property
    def mm_nucleus_mid(self) -> Dict[str, str]:
        return MM_NUCLEUS_MID

    @property
    def mm_nucleus_end(self) -> Dict[str, str]:
        return MM_NUCLEUS_END

    @property
    def mm_post_map(self) -> Dict[str, str]:
        return get_post_map()
