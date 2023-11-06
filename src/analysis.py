from typing import Dict, List


def generate_char_dictionary(char: str, words: List[str]) -> Dict[str, int]:
    d = {}
    for word in words:
        if char in word:
            all_indices = [i for i, ltr in enumerate(word) if ltr == char]
            for index in all_indices:
                if index == 0:
                    d = hit(d, word[:2])
                elif index == len(word) - 1:
                    d = hit(d, word[-2:])
                else:
                    d = hit(d, word[index : index + 2])
                    d = hit(d, word[index - 1 : index + 1])
                    d = hit(d, word[index - 1 : index + 2])
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=True))


def hit(d: Dict, comb: str):
    if d.get(comb) is not None:
        d[comb] = d[comb] + 1
    else:
        d[comb] = 1
    return d
