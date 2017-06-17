"""Split Strings Test.
mstrfx

def solution(s):
    return [s[x:x+2] if x < len(s) - 1 else s[-1] +
     "_" for x in range(0, len(s), 2)]
"""


def solution(s):
    new_s = ''
    s_list = []
    for char in s:
        new_s += char
        if len(new_s) == 2:
            s_list.append(new_s)
            new_s = ''
    if len(new_s) == 1:
        new_s += "_"
        s_list.append(new_s)
    return s_list
