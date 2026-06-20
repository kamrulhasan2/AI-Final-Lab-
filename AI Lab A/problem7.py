# 7. Write a program to find out Union and Intersection of two lists.

list1 = input("Enter first list elements separated by spaces: ").split()
list2 = input("Enter second list elements separated by spaces: ").split()

union = list(set(list1) | set(list2))
intersection = list(set(list1) & set(list2))

print("Union:", union)
print("Intersection:", intersection)
