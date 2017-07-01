"""Pyramid Slide Down.

nkrause323, Butterfly, Cod3r

def longest_slide_down(p):
    res = p.pop()
    while p:
        tmp = p.pop()
        res = [tmp[i] + max(res[i],res[i+1])  for i in range(len(tmp))]
    return res.pop()
"""


def longest_slide_down(pyramid):
    """Find longest slide down."""
    pyramid = pyramid[::-1]
    for i, row in enumerate(pyramid):
        if i > 0:
            for j, num in enumerate(row):
                row[j] += max(pyramid[i-1][j], pyramid[i-1][j+1])
    return pyramid[-1][0]
