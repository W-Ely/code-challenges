"""Complementary DNA test."""
from complementary_dna import DNA_strand


def test_complementary_dna_0_1():
    assert DNA_strand("AAAA") == "TTTT"


def test_complementary_dna_0_2():
    assert DNA_strand("ATTGC") == "TAACG"


def test_complementary_dna_0_3():
    assert DNA_strand("GTAT") == "CATA"


def test_complementary_dna_0_4():
    assert DNA_strand("TATA") == "ATAT"
