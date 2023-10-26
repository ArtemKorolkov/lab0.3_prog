from main_lab2 import decrypt_caesar
import pytest

@pytest.mark.parametrize('a,expected_result',[('SBWKRQ','PYTHON'),
                                              ('sbwkrq', 'python'),
                                              ("Sbwkrq3.6",'Python3.6'),
                                              ('1', "1"),
                                              (' '," ")])
def test_calculator(a,expected_result):
    assert decrypt_caesar(a) == expected_result
