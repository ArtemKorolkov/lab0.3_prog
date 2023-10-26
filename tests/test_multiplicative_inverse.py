from main_lab2 import multiplicative_inverse
import pytest

@pytest.mark.parametrize('a,b,expected_result',[(7,40,23),
                                                ('wfd',12,"Incorrect input")])
def test_calculator(a,b,expected_result):
    assert multiplicative_inverse(a,b) == expected_result