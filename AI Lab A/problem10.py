# 10. Write a program for finding largest and smallest element in a list.

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(number) for number in numbers]

largest = max(numbers)
smallest = min(numbers)

print("Largest element:", largest)
print("Smallest element:", smallest)
