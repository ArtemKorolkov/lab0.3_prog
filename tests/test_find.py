from sudoku import find_possible_values
from sudoku import find_empty_positions
from sudoku import read_sudoku
import pytest

@pytest.mark.parametrize('m,n,expected_result',[(read_sudoku('puzzle1.txt'), (0,2),{'1', '2', '4'}),
                                              (read_sudoku('puzzle1.txt'), (4, 7), {'2', '5', '9'})])
def test_find_possible_values(m,n,expected_result):
    assert find_possible_values(m,n) == expected_result

@pytest.mark.parametrize('m,expected_result',[([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 2)),
                                              ([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 1))])
def test_find_empty_positions(m,expected_result):
    assert find_empty_positions(m) == expected_result
