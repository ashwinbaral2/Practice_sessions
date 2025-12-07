# Q1: Print the first and last elements of a list

nums = [10, 20, 30, 40]
first = nums[0]
last = nums[-1]

print("First element:", first)
print("Last element:", last)

first = nums[0]
second = nums[1]
third = nums[2]
last = nums[-1]
print("first element:", first)
print("last element:", last)
print("second element:", second)
print("third element:", third)
# Output:
# First element: 10
# Last element: 40

# Q2: Print how many items are in the list (using len())

nums = [5, 7, 9, 11]
length = len(nums)
print("Length of list:", length)


# Output: Length of list: 4

# Q3: Print each item in the list on a new line

items = ["apple", "banana", "cherry"]
print (items[0])
print (items[1])
print (items[2])

print(items[0])
print(items[1])
print(items[2])
# Output:
# apple
# banana
# cherry

# Q4: Print index + value (no loops)

nums = [4, 7, 2]
print("Index 0:", nums[0])
print("Index 1:", nums[1])
print("Index 2:", nums[2])


# Output:
# Index 0: 4
# Index 1: 7
# Index 2: 2

# Q5: Find the largest number in the list (no max(), no loops)

nums = [3, 9, 1]

a = nums[0]
b = nums[1]
c = nums[2]

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c
print("Largest number:", largest)

# Output: Largest number: 9