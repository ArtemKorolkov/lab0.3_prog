from main_lab2 import decrypt_vigenere
import pytest

@pytest.mark.parametrize('a,key,expected_result',[('PYTHON','A','PYTHON'),
                                              ('python', 'a', 'python'),
                                              ('python3.6', 'a', 'python3.6'),
                                              ("LXFOPVEFRNHR",'LEMON', 'ATTACKATDAWN'),
                                              ('1', "v",'1'),
                                              (' '," ", ' ')])
def test_calculator(a,key,expected_result):
    assert decrypt_vigenere(a,key) == expected_result