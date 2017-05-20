"""Complementary DNA

JustyFY, ChingChangChong, pompeu2004

import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))
"""


def DNA_strand(dna):
    ref = {"A": "T", "T": "A", "G": "C", "C": "G"}
    comp = ""
    for char in dna:
        comp += ref[char]
    return comp
