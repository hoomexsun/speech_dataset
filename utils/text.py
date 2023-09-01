import io
from typing import Dict, List, Tuple
import pandas as pd


def remove_chars(content: str, chars: List[str]) -> str:
    for char in chars:
        content = content.replace(char, "")
    return content


def replace_chars(content: str, charmap: Dict[str, str]) -> str:
    for char, replacement in charmap.items():
        content = content.replace(char, replacement)
    return content


def replace_two_chars(content: str, charmap: Dict[str, str]) -> str:
    if not content:
        return ""
    output_data = []
    i = 0
    while i < len(content) - 1:
        char = content[i : i + 2]
        replacement = charmap.get(char)
        if replacement is not None:
            output_data.append(replacement)
            i += 2
        else:
            output_data.append(char[0])
            i += 1

    return "".join(output_data)


def fix_mistypes(content: str, chars: List[str], num_mistypes: int = 2) -> str:
    for char in chars:
        for num in range(num_mistypes + 1, 2, -1):
            content = content.replace(char * num, char)
    return content


def clean_s550_data(content: str) -> str:
    # insignificant_chars = "`~!@#$%^&*()_+=[]}{:;'\",.<>/?"
    insignificant_chars = "()"
    more_chars = ["\u200b", "\u200c", "\u200d", "\u200e", "\u200f", "\xad"]
    space_chars = ".,-\n\t\r\u200c"
    content = content.strip()
    content = fix_mistypes(content=content, chars=list(space_chars), num_mistypes=5)
    content = replace_chars(
        content=content, charmap={char: " " for char in space_chars}
    )
    content = remove_chars(
        content=content, chars=list(insignificant_chars) + more_chars
    )
    content = fix_mistypes(content=content, chars=[" "])
    return content


def clean_bn_data(content: str) -> str:
    insignificant_chars = "`~!@#$%^&*()_+=[]}{:;'\",.<>/?"
    more_chars = ["\u200b", "\u200c", "\u200d", "\u200e", "\u200f", "\xad"]
    space_chars = "-\n\t\r\u200c"
    content = content.strip()
    content = fix_mistypes(content=content, chars=list(space_chars), num_mistypes=5)
    content = replace_chars(
        content=content, charmap={char: " " for char in space_chars}
    )
    content = remove_chars(
        content=content, chars=list(insignificant_chars) + more_chars
    )
    content = fix_mistypes(content=content, chars=[" "])
    return content


def get_unicode_string(content: str, skip_newline: bool = False) -> str:
    ss = io.StringIO()
    for char in content:
        if char == "\n" and skip_newline:
            ss.write("\n")
        else:
            ss.write("\\u" + format(ord(char), "x").zfill(4))
    return ss.getvalue()


def pct(num: int, total: int) -> str:
    """Calculate the percentage.

    Args:
        num (int): Numerator value.
        total (int): Total value.

    Returns:
        str: Percentage value formatted as a string with two decimal places.
    """
    return format(100 * num / total, ".2f")


def unicode_as_df(content: str) -> pd.DataFrame:
    d = {}
    for char in content:
        if char in d:
            d[char]["count"] += 1
        else:
            d[char] = {
                "char": char,
                "unicode": get_unicode_string(char),
                "count": 1,
            }
    df = pd.DataFrame.from_dict(d, orient="index")
    return df


# Utterance Utility Functions
def looks_like_utt(content: str) -> bool:
    return True


def utt_lists_to_content(utt_ids: List[str], utterances: List[str]) -> str:
    return "".join(f"{utt_id}\t{utt}\n" for utt_id, utt in zip(utt_ids, utterances))


def utt_lists_to_dict(utt_ids: List[str], utterances: List[str]) -> Dict[str, str]:
    return {utt_id: utt for utt_id, utt in zip(utt_ids, utterances)}


def utt_dict_to_content(utterances_dict: Dict[str, str]) -> str:
    return "\n".join(f"{utt_id}\t{utt}" for utt_id, utt in utterances_dict.items())


def utt_content_to_dict(content: str) -> Dict[str, str]:
    if not content:
        return {}
    lines = content.split("\n")
    utt_ids, utterances = [], []
    for line in lines:
        utt_id, *utterance = line.split("\t")
        utt_ids.append(utt_id)
        utterances.extend(utterance)
    return utt_lists_to_dict(utt_ids, utterances)


def split_id_and_utt(content: str) -> Tuple[List, List]:
    lines = content.split("\n")
    utt_ids, utterances = [], []
    for line in lines:
        utt_id, *utterance = line.split("\t")
        utt_ids.append(utt_id)
        utterances.extend(utterance)
    return utt_ids, utterances
