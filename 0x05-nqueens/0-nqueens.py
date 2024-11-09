#!/usr/bin/python3
"""Solution to the N Queens problem"""

import sys


def print_solutions(solutions):
    """print all possible solutions"""
    for solution in solutions:
        print(solution)


def is_valid(board, row, col):
    """Check if queen's placement is allowed"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, row, board, solutions):
    """Recursively solve N queen"""
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return
    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)


def main():
    """Entry to program"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * N
    solve_nqueens(N, 0, board, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    """Execute main"""
    main()
