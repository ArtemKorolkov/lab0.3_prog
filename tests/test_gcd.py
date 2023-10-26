from main_lab2 import gcd
import pytest

@pytest.mark.parametrize('a,b,expected_result',[(12,15,3),
                                              (3,7, 1),
                                                ('wfd',12,"Incorrect input")])
def test_calculator(a,b,expected_result):
    assert gcd(a,b) == expected_result