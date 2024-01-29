"""https://leetcode.com/problems/valid-sudoku/"""
"""==========================================="""

# Time Complexity (TC): O(n*n) - Nested loop | Space Complexity (SC): O(n)
# The inner loops in isValidBlock iterate over each cell in a 3x3 block, but the total number of iterations is still constant (9 cells).
def isValidRow(row: list[str]) -> bool:
    seen = set()
    for elem in row:
        if elem != ".":
            if elem in seen:
                return False
            seen.add(elem)
    return True

def isValidColumn(board: list[list[str]], col_idx: int) -> bool:
    seen = set()
    for i in range(len(board)):
        elem = board[i][col_idx]
        if elem != ".":
            if elem in seen:
                return False
            seen.add(elem)
    return True

def isValidBlock(board: list[list[str]], start_row: int, start_col: int) -> bool:
    seen = set()
    for i in range(3):
        for j in range(3):
            elem = board[start_row + i][start_col + j]
            if elem != ".":
                if elem in seen:
                    return False
                seen.add(elem)
    return True

def isValidSudoku(board: list[list[str]]) -> bool:
    # Check rows
    for i in range(len(board)):
        if not isValidRow(board[i]):
            return False

    # Check columns
    for j in range(len(board[0])):
        if not isValidColumn(board, j):
            return False

    # Check 3x3 blocks
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not isValidBlock(board, i, j):
                return False

    return True
