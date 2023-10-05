def swap(data: str, pair: str) -> str:
    char_list = list(data)
    index = data.find(pair)

    while index != -1:
        char_list[index], char_list[index + 1] = char_list[index + 1], char_list[index]
        index = data.find(pair, index + 2)  # Start searching after the current pair

    return "".join(char_list)


# Test case 1: Swap 'AB' with 'BA' in the string
data1 = "ABCDEABFGHIAB"
pair1 = "AB"
result1 = swap(data1, pair1)
print(result1)  # Should print "BACDEBAFGHIBA"

# Test case 2: Swap '12' with '21' in the string
data2 = "1212121212"
pair2 = "12"
result2 = swap(data2, pair2)
print(result2)  # Should print "2121212121"

# Test case 3: No swap should occur as the pair is not found
data3 = "ABCDEFG"
pair3 = "XY"
result3 = swap(data3, pair3)
print(result3)  # Should print "ABCDEFG"

# Test case 4: Swap 'CD' with 'DC' in the string
data4 = "CDCDCD"
pair4 = "CD"
result4 = swap(data4, pair4)
print(result4)  # Should print "DCCDCD"

# Test case 5: Swap 'AB' with 'BA' multiple times in the string
data5 = "ABBABBAB"
pair5 = "AB"
result5 = swap(data5, pair5)
print(result5)  # Should print "BAABABBA"
