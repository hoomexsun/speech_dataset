def transliteration(line, BCC, MMArr, BArr):
    output = []
    for tline in line:
        if tline == " ":
            output.append(" ")
        else:
            pos = None
            for index, b_char in enumerate(BArr):
                if tline == b_char:
                    pos = index
                    break
            if pos is not None:
                output.append(MMArr[pos])
    return "".join(output)


# Example usage:
MMArr = [
    "Meitei1",
    "Meitei2",
    "Meitei3",
    "...",
]  # Replace with actual Meitei Mayek characters list
BArr = [
    "Bengali1",
    "Bengali2",
    "Bengali3",
    "...",
]  # Replace with actual Bengali characters list
BCC = len(BArr)
line = "Bengali Text to Transliterate"  # Replace with your Bengali input
result = transliteration(line, BCC, MMArr, BArr)
print(result)
