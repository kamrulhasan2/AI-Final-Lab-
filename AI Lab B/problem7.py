# 7. Write a program to implement the hill climbing algorithm.


def objective_function(x):
    return -(x - 3) ** 2 + 10


current = 0
step_size = 1

while True:
    left = current - step_size
    right = current + step_size

    if objective_function(left) > objective_function(current):
        current = left
    elif objective_function(right) > objective_function(current):
        current = right
    else:
        break

print("Best value of x:", current)
print("Maximum objective value:", objective_function(current))
