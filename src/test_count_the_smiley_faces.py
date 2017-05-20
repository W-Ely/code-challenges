"""Count the smiley faces tests"""
from count_the_smiley_faces import count_smileys


def test_count_the_smiley_faces_0_0():
    """Empty list."""
    assert count_smileys([]) == 0


def test_count_the_smiley_faces_0_1():
    """All Smiles."""
    assert count_smileys([':D', ':~)', ';~D', ':)']) == 4


def test_count_the_smiley_faces_0_3():
    """Some not smiles"""
    assert count_smileys([':)', ':(', ':D', ':O', ':;']) == 2


def test_count_the_smiley_faces_0_4():
    """Diff Chars."""
    assert count_smileys([';]', ':[', ';*', ':$', ';-D']) == 1


def test_count_the_smiley_faces_0_5():
    """Non-sense."""
    assert count_smileys(['<><', '<56', '*', '65', 'dsf']) == 0
