#!/usr/bin/python3
"""Module defines a solution to the N queens problem"""
import sys


def is_safe(board, row, col):
    """Checks if queen can b placed at given position"""
    for i in range(row):
        """checking if there's a queen in that column"""
        if board[i] == col:
            return False
        """checking if there's a queen in the diagonal"""
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(board, row, n):
    """Solves n_queens after all queens have bn placed"""
    if row == n:
        print_board(board, n)
        return
    """(Trial) Place queen in each column for current row"""
    for col in range(n):
        if is_safe(board, row, col):
            """places quen at current position if it's safe"""
            board[row] = col
            """Solving for the next row (Recursion)"""
            solve_nqueens(board, row + 1, n)
            """Backtrack and move queen from current position"""
            board[row] = -1


def print_board(board, n):
    """Prints current solution"""
    queens = [[i, board[i]] for i in range(n)]
    print(queens)


def nqueens(n):
    """Ensures n is an int"""
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
