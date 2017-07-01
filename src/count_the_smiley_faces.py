"""Count the smiley faces.

betegelse

from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))
"""


def count_smileys(arr):
    """Count the smiles."""
    total = 0
    for item in arr:
        smile = True
        for i, char in enumerate(item):
            if i == 0 and char != ":" and char != ";":
                smile = False
            if i == 1 and len(item) == 2 and char != ")" and char != "D":
                smile = False
            if i == 1 and len(item) == 3 and char != "-" and char != "~":
                smile = False
            if i == 2 and char != ")" and char != "D":
                smile = False
        if smile:
            total += 1
    return total
