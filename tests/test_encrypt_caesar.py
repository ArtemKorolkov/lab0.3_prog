from main_lab2 import encrypt_caesar
import pytest

@pytest.mark.parametrize('a,expected_result',[('PYTHON','SBWKRQ'),
                                              ('python', 'sbwkrq'),
                                              ("Python3.6",'Sbwkrq3.6'),
                                              ('1', "1"),
                                              (' '," ")])
def test_calculator(a,expected_result):
    assert encrypt_caesar(a) == expected_result