# Creating a list of strings
fruits = ["apple", "banana", "cherry"]

# Creating a mixed-type list
mixed_list = [10, "Python", 3.14, True]

# Creating an empty list
List = []
print("Blank List:", List)

# Creating a list of numbers
List = [10, 20, 14]
print("List of numbers:", List)

# Creating a list of strings
List = ["Geeks", "For", "Geeks"]
print("First element:", List[0])  # Output: Geeks
print("Third element:", List[2])  # Output: Geeks

# Accessing list elements
numbers = [10, 20, 30, 40, 50]
print(numbers[0])   # Output: 10 (first element)
print(numbers[-1])  # Output: 50 (last element)

# Modifying an element (lists are mutable)
numbers[1] = 99
print(numbers)  # Output: [10, 99, 30, 40, 50]

# Slicing a list: [start:stop]
print(numbers[1:4])  # Output: [99, 30, 40] (index 4 excluded)

# Adding elements using append()
items = ["pen", "paper"]
items.append("eraser")  # Adds an element at the end
print(items)  # Output: ['pen', 'paper', 'eraser']

# Adding elements using insert()
items.insert(1, "pencil")  # Inserts at index 1
print(items)  # Output: ['pen', 'pencil', 'paper', 'eraser']

# Adding multiple elements using extend()
items.extend(["ruler", "ink"])  # Adds each element individually
print(items)  # Output: ['pen', 'pencil', 'paper', 'eraser', 'ruler', 'ink']

# Removing and returning the last element using pop()
colors = ["red", "green", "blue", "green"]
last_color = colors.pop()
print(last_color)  # Output: green
print(colors)  # Output: ['red', 'green', 'blue']

# Removing the first occurrence of a value
colors.remove("green")
print(colors)  # Output: ['red', 'blue']

# Removing all elements from a list
colors.clear()
print(colors)  # Output: []

# Counting occurrences of an element
scores = [45, 82, 12, 82, 90]
print(scores.count(82))  # Output: 2

# Finding the index of the first occurrence
print(scores.index(12))  # Output: 2

# Sorting elements in ascending order
scores.sort()
print(scores)  # Output: [12, 45, 82, 82, 90]

# Reversing the current order
scores.reverse()
print(scores)  # Output: [90, 82, 82, 45, 12]

# Built-in functions used with lists
nums = [3, 1, 4, 1, 5]
print(len(nums))  # Output: 5 (number of elements)
print(max(nums))  # Output: 5 (largest element)
print(min(nums))  # Output: 1 (smallest element)
print(sum(nums))  # Output: 14 (sum of elements)

# Creating a list of squares using a for loop
squares = []
for x in range(1, 6):
    squares.append(x**2)  # Adds the square of x to the list
print(squares)  # Output: [1, 4, 9, 16, 25]

# Creating the same list using list comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]