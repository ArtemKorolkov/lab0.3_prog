from main_lab2 import encrypt_vigenere
import pytest

@pytest.mark.parametrize('a,key,expected_result',[('PYTHON','A','PYTHON'),
                                              ('python', 'a', 'python'),
                                              ('python3.6', 'a', 'python3.6'),
                                              ("ATTACKATDAWN",'LEMON', 'LXFOPVEFRNHR'),
                                              ('1', "v",'1'),
                                              (' '," ", ' ')])
def test_calculator(a,key,expected_result):
    assert encrypt_vigenere(a,key) == expected_result