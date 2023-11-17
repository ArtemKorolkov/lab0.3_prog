from sudoku import get_row
from sudoku import get_col
from sudoku import get_block
from sudoku import read_sudoku
import pytest

@pytest.mark.parametrize('m,n,expected_result',[([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0), ['4', '.', '6']),
                                              ([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0), ['1', '2', '.'])])
def test_get_row(m,n,expected_result):
    assert get_row(m,n) == expected_result

@pytest.mark.parametrize('m,n,expected_result',[([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0), ['1', '4', '7']),
                                              ([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1), ['2', '.', '8'])])
def test_get_col(m,n,expected_result):
    assert get_col(m,n) == expected_result


@pytest.mark.parametrize('m,n,expected_result',[(read_sudoku('puzzle1.txt'), (0, 1),['5', '3', '.', '6', '.', '.', '.', '9', '8']),
                                              (read_sudoku('puzzle1.txt'),(4, 7),['.', '.', '3', '.', '.', '1', '.', '.', '6'])])
def test_get_block(m,n,expected_result):
    assert get_block(m,n) == expected_result