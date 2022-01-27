# Pytest
from unit_testing.simplecalc import SimpleCalc


def test_calc_add():
    calc = SimpleCalc()
    assert calc.add(2, 6) == 8

