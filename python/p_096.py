# problem 96 - 2026.02.07 - Solution by Dominik Szombathy
# Difficulty level - 5
# Solution = 24702


import numpy as np

def read_sudoku_file(filename: str) -> dict:
    puzzles = {}

    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    
    i = 0
    while i < len(lines):
        if lines[i].startswith("Grid"):
            grid_name = lines[i]
            board_lines = lines[i + 1:i + 10]

            grid = np.array([[int(ch) for ch in row] for row in board_lines])
            puzzles[grid_name] = grid
            i += 10
        else:
            i += 1

    return puzzles

def collaps_based_on_element(solution: list, element: int, row: int, col: int) -> None:
    for c in range(9):
        if c != col and isinstance(solution[row][c], list):
            if element in solution[row][c]:
                solution[row][c].remove(element)
    for r in range(9):
        if r != row and isinstance(solution[r][col], list):
            if element in solution[r][col]:
                solution[r][col].remove(element)
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if (r != row or c != col) and isinstance(solution[r][c], list):
                if element in solution[r][c]:
                    solution[r][c].remove(element)

def solve_sudoku(sudoku: np.ndarray) -> list:
    Elements = list(range(1, 10))
    solution = [[Elements.copy() for _ in range(9)] for _ in range(9)]
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] > 0:
                solution[row][col] = sudoku[row][col]
                collaps_based_on_element(solution, sudoku[row][col], row, col)
    return solution

def is_solved(solution: list) -> bool:
    for r in range(9):
        for c in range(9):
            if isinstance(solution[r][c], list):
                return False
    return True

def find_singletons(solution: list) -> bool:
    updated = False
    for r in range(9):
        for c in range(9):
            if isinstance(solution[r][c], list) and len(solution[r][c]) == 1:
                val = solution[r][c][0]
                solution[r][c] = val
                collaps_based_on_element(solution, val, r, c)
                updated = True
    return updated

def solve_full_sudoku(sudoku: np.ndarray) -> list:
    solution = solve_sudoku(sudoku)
    progress = True
    while progress:
        progress = find_singletons(solution)
    # Backtracking if needed
    return backtrack(solution)

def copy_solution(solution: list) -> list:
    return [[cell.copy() if isinstance(cell, list) else cell for cell in row] for row in solution]

def backtrack(solution: list) -> list:
    for r in range(9):
        for c in range(9):
            if isinstance(solution[r][c], list):
                for val in solution[r][c]:
                    trial = copy_solution(solution)
                    trial[r][c] = val
                    collaps_based_on_element(trial, val, r, c)
                    trial_solved = backtrack(trial)
                    if trial_solved is not None:
                        return trial_solved
                return None
    return solution

def get_first_3_numbers(solution):
    vals = []
    for c in range(3):
        v = solution[0][c]
        if isinstance(v, list):
            if not v:
                raise ValueError(f"Cell (0,{c}) has no candidates")
            v = v[0]
        vals.append(int(v))
    return vals[0] * 100 + vals[1] * 10 + vals[2]


# Example usage
puzzles = read_sudoku_file("Data/0096_sudoku.txt")

sum = 0
for names in puzzles:
    sum += get_first_3_numbers(solve_full_sudoku(puzzles[names]))

print(sum)