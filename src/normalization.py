# Text Normalization Functions
from typing import List


def normalize_abbrev(word: str) -> str:
    expanded = ""
    return expanded


en_abbrev_map = {}
bn_abbrev_map = {}
mm_abbrev_map = {}


def normalize_number(word: str) -> str:
    if ":" in word:
        return as_time(word)
    elif word[0] == "0":
        return as_digit(word)
    else:
        return as_number(word[1:])


def as_time(word):
    return ""


def as_digit(word):
    word = mm_to_en_digits(word)
    return " ".join([num_map(digit) for digit in word])


# An algorithm here
def as_number(word):
    reversed_word = mm_to_en_digits(word)[::-1]
    # print(f"Start | {word=}  | {reversed_word=} ")
    paired_list: List[str] = []
    paired_list.append(reversed_word[:2][::-1])
    # print(f"First | {reversed_word[:2][::-1]}")
    if len(reversed_word) > 2:
        paired_list.append(reversed_word[2])
        # print(f"Hundred | {reversed_word[2]}")
        for i, char in enumerate(reversed_word[3:]):
            if i == len(reversed_word) - 4:
                paired_list.append(char)
                # print(f"Single | {char=}")
            elif i % 2 == 0:
                paired_list.append(reversed_word[i + 4] + char)
                # print(f"Pair | {reversed_word[i + 4] + char}")
    print(f"{word=}  | {reversed_word=} | {paired_list=}")
    output = [
        fix_place_value(fix_digit(pair, index == 1), index)
        for index, pair in enumerate(paired_list)
    ]
    output = " ".join(output[::-1])
    return output


def fix_digit(element: str, is_hundred: bool = False):
    if is_hundred:
        return num_map(element[0], 3)
    if len(element) == 1:
        return num_map(element[0], 0)
    if element[0] == "0":
        return num_map(element[0], 2) + " " + num_map(element[1], 0)
        # return num_map(element[1], 0)
    return num_map(element[0], 2) + " " + num_map(element[1], 1)


def fix_place_value(element: str, index: int):
    if index < 2:
        return element
    if index == 2:
        return "ꯂꯤꯁꯤꯡ " + element
    if index == 3:
        return "ꯂꯥꯛ " + element
    if index == 4:
        return "ꯀꯔꯣꯔ " + element
    return element


def mm_to_en_digits(digits: str) -> str:
    mm = ("꯰", "꯱", "꯲", "꯳", "꯴", "꯵", "꯶", "꯷", "꯸", "꯹")
    result = int("".join([str(mm.index(digit)) for digit in digits]))
    return str(result)


def bn_to_en_digits(digits: str) -> str:
    bn = ("০", "১", "২", "৩", "৪", "৫", "৬", "৭", "৮", "৯")
    output = int("".join([str(bn.index(digit)) for digit in digits]))
    return str(output)


def num_map(key: str, pos: int = 0) -> str:
    if key not in mm_nummap or pos > 3:
        return key
    else:
        return mm_nummap[key][pos]


mm_nummap = {
    "0": ("ꯁꯤꯅꯣ", "", "ꯒ", "ꯒ"),
    "1": ("ꯑꯃ", "ꯃꯥꯊꯣꯢ", "ꯇꯔꯥ", "ꯆꯥꯝꯃ"),
    "2": ("ꯑꯅꯤ", "ꯅꯤꯊꯣꯢ", "ꯀꯨꯟ", "ꯆꯥꯅꯤ"),
    "3": ("ꯑꯍꯨꯝ", "ꯍꯨꯝꯗꯣꯢ", "ꯀꯨꯟꯊ꯭ꯔꯥ", "ꯆꯥꯍꯨꯝ"),
    "4": ("ꯃꯔꯤ", "ꯃꯔꯤ", "ꯅꯤꯐꯨ", "ꯆꯥꯃꯔꯤ"),
    "5": ("ꯃꯉꯥ", "ꯃꯉꯥ", "ꯌꯥꯡꯈꯩ", "ꯆꯥꯝꯉꯥ"),
    "6": ("ꯇꯔꯨꯛ", "ꯇꯔꯨꯛ", "ꯍꯨꯝꯐꯨ", "ꯆꯥꯇ꯭ꯔꯨꯛ"),
    "7": ("ꯇꯔꯦꯠ", "ꯇꯔꯦꯠ", "ꯍꯨꯝꯐꯨꯇꯔꯥ", "ꯆꯥꯇ꯭ꯔꯦꯠ"),
    "8": ("ꯅꯤꯄꯥꯜ", "ꯅꯤꯄꯥꯜ", "ꯃꯔꯤꯐꯨ", "ꯆꯥꯅꯤꯄꯥꯜ"),
    "9": ("ꯃꯥꯄꯜ", "ꯃꯥꯄꯜ", "ꯃꯔꯤꯐꯨ", "ꯆꯥꯃꯥꯄꯜ"),
}


def main():
    print(as_number("꯰"))
    print(as_number("꯱"))
    print(as_number("꯵"))
    print(as_number("꯰꯵"))
    print(as_number("꯱꯱"))
    print(as_number("꯱꯵"))
    print(as_number("꯲꯵"))
    print(as_number("꯱꯲꯵"))
    print(as_number("꯱꯰꯵"))
    print(as_number("꯲꯱꯲꯵"))
    print(as_number("꯲꯰꯲꯵"))
    print(as_number("꯲꯱꯰꯵"))
    print(as_number("꯳꯲꯱꯲꯵"))
    print(as_number("꯶꯳꯲꯱꯲꯵"))
    print(as_number("꯸꯶꯳꯲꯱꯲꯵"))
    print(as_number("꯸꯶꯳꯲꯱꯲꯲꯱꯲꯵"))


if __name__ == "__main__":
    main()
