# 2. Write a program for finding the sum of all numbers in a given list.

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(number) for number in numbers]

total = sum(numbers)

print("Sum of all numbers:", total)
