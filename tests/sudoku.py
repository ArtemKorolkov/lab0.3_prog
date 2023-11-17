import pathlib
import typing as tp
import random
T = tp.TypeVar("T")

import sys
sys.setrecursionlimit(3000)

def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    #реализация при помощи лабы
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    #формирование массива массивов n на n
    res=[[] for i in range(n)]
    c=0
    l=0
    for i in range(n):
        for j in range(n):
            res[c].append(values[l])
            l+=1
        c+=1
    return res
print(group([1,2,3,4,5,6,7,8,9], 3))

def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return grid[pos[0]] #возврат значений по указанному номеру строки
print(get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0)))


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    # возврат значений по указанному номеру столбца
    res=[]
    for i in grid:
        for j in range(len(i)):
            if j==pos[1]:
                res.append(i[j])
    return res
print(get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1)))


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    res=[]
    #выбор строки, с которой начинается блок, в который входит значение
    if pos[0] < 3:
        c = 0
    elif pos[0] >5:
        c=6
    else:
        c=3
    #выбор столбца, с которой начинается блок, в который входит значение
    if pos[1] < 3:
        start_st = 0
    elif pos[1]>5:
        start_st=6
    else:
        start_st=3
    for i in range(3):
        st=start_st
        for j in range(3):
            res.append(grid[c][st])
            st+=1
        c+=1

    return res
print(read_sudoku('puzzle1.txt'))
grid = read_sudoku('puzzle1.txt')
print(get_block(grid, (0, 1)))


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    #поиск незаполненных значений (возврат 1-ой ".")
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]=='.':
                return (i,j)
print(find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]))


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    global i
    sp=['1','2','3','4','5','6','7','8','9']
    row=get_row(grid,pos)
    col=get_col(grid,pos)
    block=get_block(grid,pos)
    not_res=[]
    for i in row:
        if i.isnumeric():
            not_res.append(i)
    for i in col:
        if i.isnumeric():
            not_res.append(i)
    for i in block:
        if i.isnumeric():
            not_res.append(i)
    not_res=list(set(not_res))
    val=set()
    for i in sp:
        if i not in not_res:
            val.add(i)
    return val
print(find_possible_values(grid, (4,7)))


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    free_pos = find_empty_positions(grid)
    if free_pos is None:
        return grid if check_solution(grid) else None

    possible_values = find_possible_values(grid, free_pos)
    for possible_value in possible_values:
        last_value = grid[free_pos[0]][free_pos[1]]

        grid[free_pos[0]][free_pos[1]] = possible_value

        solution = solve(grid)
        if solution is not None:
            return solution

        grid[free_pos[0]][free_pos[1]] = last_value

    return None

def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    # TODO: Add doctests with bad puzzles
    lines = []
    lines += [get_row(solution, (i, 0)) for i in range(len(solution))]
    lines += [get_col(solution, (0, i)) for i in range(len(solution[0]))]
    lines += [
        get_block(solution, (y, x))
        for y in range(0, len(solution), 3)
        for x in range(0, len(solution[y]), 3)
    ]

    for line in lines:
        line = list(set(line))
        if "." in line or len(line) != len(solution):
            return False

    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    grid = [["."] * 9 for _ in range(9)]
    solution = solve(grid)

    grid = solution

    free_poses = [(y, x) for y in range(len(grid)) for x in range(len(grid[y]))]
    for _ in range(len(grid) * len(grid[0]) - N):
        index_pos = random.randint(0, len(free_poses) - 1)
        pos = free_poses[index_pos]
        del free_poses[index_pos]

        grid[pos[0]][pos[1]] = "."

    return grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)

#ускорение и замер решения
import threading
import time
def run_solve(filename: str) -> None:
    grid = read_sudoku(filename)
    start = time.time()
    solve(grid)
    end = time.time()
    print(f"{filename}: {end-start}")

if __name__ == "__main__":
    for filename in ("puzzle1.txt", "puzzle2.txt", "puzzle3.txt"):
        t = threading.Thread(target=run_solve, args=(filename,))
        t.start()

import multiprocessing

if __name__ == "__main__":
    for filename in ("puzzle1.txt", "puzzle2.txt", "puzzle3.txt"):
        p = multiprocessing.Process(target=run_solve, args=(filename,))
        p.start()