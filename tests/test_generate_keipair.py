from main_lab2 import generate_keypair
import pytest

@pytest.mark.parametrize('a,b,expected_result',[('wfd',5,"Incorrect input")])
def test_calculator(a,b,expected_result):
    assert generate_keypair(a,b) == expected_result