"""Most Digits

Unnamed, Superior.Sukh

def find_longest(xs):
    return max(xs, key=lambda x: len(str(x)))
"""


def find_longest(arr):
    longest = ''
    arr.reverse()
    for num in arr:
        if len(str(num)) >= len(longest):
            longest = str(num)
    arr.reverse()
    return int(longest)
