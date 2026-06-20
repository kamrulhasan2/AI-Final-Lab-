# 8. Write a program to determine the Greatest Common Divisor of two 
# positive integer numbers.

num1 = int(input("Enter first positive integer: "))
num2 = int(input("Enter second positive integer: "))

a = num1
b = num2

while b != 0:
    a, b = b, a % b

print("Greatest Common Divisor:", a)
