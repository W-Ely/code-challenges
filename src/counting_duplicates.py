"""Counting Duplicates

tpatja, nkrause323, alpen0

def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
"""


def duplicate_count(text):
    u = set()
    for char in text:
        if text.lower().count(char) >= 2:
            u.add(char)
    return len(u)
