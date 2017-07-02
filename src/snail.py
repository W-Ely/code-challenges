"""Snail.

foxxyz, JasonFTW, Aweson2, polarizing, __TomFoolery__, robodia2017

def snail(array):
    return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []
"""


def snail(snail_input):
    """Return array snail of given array of arrays."""
    snail = []
    while snail_input:
        snail += snail_input.pop(0)
        for line in snail_input:
            if line:
                if line is not snail_input[-1]:
                    snail += [line.pop()]
        if snail_input:
            snail += snail_input.pop()[::-1]
        for line in snail_input[::-1]:
            if line and line is not snail_input[0]:
                snail += [line.pop(0)]
    return snail
