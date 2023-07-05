#!/usr/bin/python3
"""
This program solves the N Queens problem.
The N Queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
"""
from sys import argv


if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided.
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    # Check if the argument is a valid integer.
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)

    # Check if N is less than 4.
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # Initialize the list to store the solutions.
    solutions = []
    for i in range(n):
        solutions.append([i, None])

    # Print every possible solution to the problem, one solution per line.
    def exist_or_not(position):
        """
        checks if a queen exits in a spesific position or not.
        """
        for i in range(n):
            if position == solutions[i][1]:
                return True
        return False

    def reject_solution_or_not(sol, position):
        """
        checks whather to reject a solution or not.
        """
        if exist_or_not(position):
            return False
        i = 0
        while i < sol:
            if abs(solutions[i][1] - position) == abs(i - sol):
                return False
            i += 1
        return True

    def clear_solutions(sol):
        """
        clears solutions.
        """
        for i in range(sol, n):
            solutions[i][1] = None

    def nqueens(sol):
        """
        a recursive backtracking function to find solutions.
        """
        for i in range(n):
            clear_solutions(sol)
            if reject_solution_or_not(sol, i):
                solutions[sol][1] = i
                # Print the solution.
                if sol == n - 1:
                    print(solutions)
                # Move to the next row and continue solving recursively.
                else:
                    nqueens(sol + 1)

    nqueens(0)
