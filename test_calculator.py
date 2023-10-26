from main import calculator
import pytest

@pytest.mark.parametrize('a,expected_result',[('4 + 6',10),
                                              ('6 / 6', 1),
                                              ("5 % 4",1),
                                              ('10 // 0', "Ошибка! Проверьте точность данных"),
                                              ('1223',"Неверный формат ввода")])
def test_calculator_good(a,expected_result):
    assert calculator(a) == expected_result
