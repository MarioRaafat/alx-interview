#!/usr/bin/python3
import sys


def check_input():
    """Check and validate the input argument."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    number = sys.argv[1]
    if not number.isdigit():
        print("N must be a number")
        sys.exit(1)

    number = int(number)
    if number < 4:
        print("N must be at least 4")
        sys.exit(1)

    return number


def is_safe(row, column, solution):
    """Check if a queen can be placed at (row, column)."""
    for c, r in solution:
        if r == row or abs(r - row) == abs(c - column):
            return False
    return True


def get_solutions(n, solutions, solution, col):
    """Recursively find all valid solutions for N-Queens."""
    if col == n:
        solutions.append(solution.copy())
        return

    for row in range(n):
        if is_safe(row, col, solution):
            solution.append([col, row])
            get_solutions(n, solutions, solution, col + 1)
            solution.pop()


def nqueens():
    """Main function to solve the N-Queens problem."""
    n = check_input()
    solutions = []
    get_solutions(n, solutions, [], 0)

    for ele in solutions:
        print(ele)


if __name__ == "__main__":
    nqueens()
