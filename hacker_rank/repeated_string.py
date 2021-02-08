
def repeatedString(string, n):

    string_as = string.count("a")
    whole_repeats = n // len(string)

    rem = n % len(string)
    rem_as = string[:rem].count("a")

    total_as = (whole_repeats * string_as) + rem_as
    return total_as

print(repeatedString("abcac", 10))
print(repeatedString("aba", 10))
print(repeatedString("a", 1000000000))


