# Pytest
from unit_testing.simplecalc import SimpleCalc
import pytest


def test_calc_add():
    calc = SimpleCalc()
    assert calc.add(2, 6) == 8


def test_calc_multiply():
    calc = SimpleCalc()
    assert pytest.approx(calc.multiply(0.4, -80.9)) == -32.36
    # assert pytest.approx(calc.multiply(0.4, -80.9), 0.000001) == -32.36  # 0.000001 means (+) or (-) 0.000001 from actual answer


def test_calc_multiply_by_zero_raises_error():
    calc = SimpleCalc()
    with pytest.raises(ZeroDivisionError):
        calc.divide(2, 0)
