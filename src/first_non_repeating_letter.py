"""First non-repeating letter

tachyonlabs

def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]

    return ""
"""


def first_non_repeating_letter(string):
    new_string = string[:]
    string = string.lower()
    for i, char in enumerate(string):
        if string.count(char) == 1:
            return new_string[i]
    return ""
