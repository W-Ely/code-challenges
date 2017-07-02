"""Module tests proper_paranthetics kata."""
from proper_parenthetics import proper_paranthetics


def test_correct_order():
    """Test return 0 for balanced."""
    assert proper_paranthetics('(sgtsr)(sss)(ystystr)') == 0


def test_incorrect_order_open():
    """Test return 1 for open."""
    assert proper_paranthetics('(stysty)stysy(ssy)(tryt') == 1


def test_broken():
    """Test return -1 for balanced."""
    assert proper_paranthetics('syts)sty(tysy665)(s6y56y)') == -1


def test_correct_order_combo():
    """Test return 0 for balanced."""
    assert proper_paranthetics(r"(sgt{s}r)(sss)(yst<ys>tr)") == 0


def test_incorrect_order_open_combo():
    """Test return 1 for open."""
    assert proper_paranthetics('(stysty)st<ys>y(ssy)(tryt') == 1


def test_broken_combo():
    """Test return -1 for balanced."""
    assert proper_paranthetics('sy<ts>)sty(tysy665)(s6y56y)') == -1


def test_wrong_order():
    """Test wrong order is broken."""
    assert proper_paranthetics('<afd>({)}') == -1
