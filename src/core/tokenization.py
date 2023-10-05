# TODO: Tokenization


from typing import Callable, List

NUMBERS = "0123456789"
NUMBERS_FORMAT = NUMBERS + ":"


def tokenize_number(word: str) -> str:
    result = []
    for current_char, next_char in zip(word, word[1:]):
        result.append(current_char)
        if (current_char in NUMBERS_FORMAT) != (next_char in NUMBERS_FORMAT):
            result.append(" ")
    result.append(word[-1])
    return "".join(result)


def test(func: Callable, input_str: str):
    print(f"{input_str=}")
    output_str = func(input_str)
    print(f"{output_str=}")


if __name__ == "__main__":
    test(tokenize_number, "1000ga")
    test(tokenize_number, "ei1000ga")
    test(tokenize_number, "ei1000")
    test(tokenize_number, "ei10:00")
    test(tokenize_number, "ei1000ga2")
    test(tokenize_number, "ei1000ga2bi")
