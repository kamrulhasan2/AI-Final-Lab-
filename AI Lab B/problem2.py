# 2. Write a program to solve 8-puzzle problem.

from collections import deque


START = (1, 2, 3, 4, 0, 6, 7, 5, 8)
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def print_board(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


def get_neighbors(state):
    zero = state.index(0)
    row, col = divmod(zero, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
            neighbors.append(tuple(new_state))

    return neighbors


def solve_puzzle(start, goal):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None


solution = solve_puzzle(START, GOAL)

if solution:
    print("8-Puzzle solution:")
    for step in solution:
        print_board(step)
else:
    print("No solution found.")
