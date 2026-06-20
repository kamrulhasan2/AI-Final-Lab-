# 1. Write a program to solve 4-queen problem.

N = 4
board = [["." for _ in range(N)] for _ in range(N)]


def is_safe(row, col):
    for i in range(row):
        if board[i][col] == "Q":
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve(row):
    if row == N:
        return True

    for col in range(N):
        if is_safe(row, col):
            board[row][col] = "Q"
            if solve(row + 1):
                return True
            board[row][col] = "."

    return False


if solve(0):
    print("Solution for 4-Queen problem:")
    for row in board:
        print(" ".join(row))
else:
    print("No solution found.")
