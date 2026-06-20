# 4. Write a program to solve the traveling salesman problem.

from itertools import permutations


graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
]

start_city = 0
cities = [1, 2, 3]
minimum_cost = float("inf")
best_path = None

for order in permutations(cities):
    path = [start_city] + list(order) + [start_city]
    cost = 0

    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]

    if cost < minimum_cost:
        minimum_cost = cost
        best_path = path

print("Best path:", best_path)
print("Minimum cost:", minimum_cost)
