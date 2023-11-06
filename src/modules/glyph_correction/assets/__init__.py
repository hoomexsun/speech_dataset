from typing import Dict, List

from .s550_bn_map import (
    BN_ALPHABET,
    BN_COMPLETE,
    BN_EXTRA,
    BN_INCOMPLETE,
    BN_PSEUDO_ALPHABET,
    BN_PUNCTUATION,
    BN_R_RIGHT,
    BN_VOWEL_DOWN,
    BN_VOWEL_LEFT,
    BN_VOWEL_OUTSIDE,
    BN_VOWEL_RIGHT,
    EN_PUNCTUATIONS,
    S550_ADJUST,
    S550_INSIGNIFICANT_CHARS,
)

__all__ = ["Resource"]


class Resource:
    def bn_map(self) -> Dict[int, Dict[str, str]]:
        bn_dict = {
            **BN_ALPHABET,
            **BN_PSEUDO_ALPHABET,
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
    def bn_dependent_vowels(self) -> List[str]:
        bn_vowel_nucleus = {
            **BN_VOWEL_LEFT,
            **BN_VOWEL_RIGHT,
            **BN_VOWEL_DOWN,
            **BN_VOWEL_OUTSIDE,
        }
        return list({vowel for vowel in bn_vowel_nucleus.values()})

    @property
    def bn_dependent_consonants(self) -> List[str]:
        bn_consonant_coda = {**BN_PSEUDO_ALPHABET}
        return list({vowel for vowel in bn_consonant_coda.values()})

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
        return BN_VOWEL_OUTSIDE

    @property
    def en_punctuations(self) -> List[str]:
        return list(EN_PUNCTUATIONS)

    @property
    def s550_insignificant_chars(self) -> List[str]:
        return list(S550_INSIGNIFICANT_CHARS)
