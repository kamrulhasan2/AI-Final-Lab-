# 8. Write a program to sort a list.

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(number) for number in numbers]

numbers.sort()

print("Sorted list:", numbers)
