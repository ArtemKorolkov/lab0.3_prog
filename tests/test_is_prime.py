from main_lab2 import is_prime
import pytest

@pytest.mark.parametrize('a,expected_result',[(1,True),
                                              (2, True),
                                              (11,True),
                                              (8, False),
                                              ('wfd',"It's not a number")])
def test_calculator(a,expected_result):
    assert is_prime(a) == expected_result