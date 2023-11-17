from sudoku import group
import pytest

@pytest.mark.parametrize('m,n,expected_result',[([1,2,3,4],2,[[1, 2], [3, 4]]),
                                              ([1,2,3,4,5,6,7,8,9],3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])])
def test_group(m,n,expected_result):
    assert group(m,n) == expected_result