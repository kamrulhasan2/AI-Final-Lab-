# 5. Write a program to determine whether an element is a member of a list.

items = input("Enter list elements separated by spaces: ").split()
element = input("Enter element to search: ")

if element in items:
    print(element, "is a member of the list.")
else:
    print(element, "is not a member of the list.")
