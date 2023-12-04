from main import analiz
import pytest

@pytest.mark.parametrize('input,expected_result',[('1,2', 'Дюна'),
                                              ('2,4','Дюна')])
def test_N1(input,expected_result):
    assert analiz.recomend(input) == expected_result