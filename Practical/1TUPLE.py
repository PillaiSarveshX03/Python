# 1. Creating an empty tuple
my_tuple = ()
print(my_tuple)  # Output: ()

# 2. Creating a tuple of integers
my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)

# 3. Creating a tuple with mixed data types
my_tuple = (1, "Hello", 3.4)
print(my_tuple)  # Output: (1, 'Hello', 3.4)

# 4. Accessing elements using indexing
dimensions = (10, 20, 30, 40)
print(dimensions[0])   # Output: 10
print(dimensions[-1])  # Output: 40

# 5. Slicing a tuple
print(dimensions[1:3])  # Output: (20, 30)

# 6. Counting occurrences of a value
values = (1, 2, 3, 2, 4, 2)
print(values.count(2))  # Output: 3

# 7. Finding the index of a value
print(values.index(4))  # Output: 4


# ==================== EXTRA TOPICS ====================

# 8. Single-element tuple                         # EXTRA
t = (5,)
print(t)        # Output: (5,)
print(type(t))  # Output: <class 'tuple'>

# 9. Built-in functions                           # EXTRA
nums = (10, 20, 30, 40)
print(len(nums))     # Output: 4
print(max(nums))     # Output: 40
print(min(nums))     # Output: 10
print(sum(nums))     # Output: 100
print(sorted(nums))  # Output: [10, 20, 30, 40] (returns a list)

# 10. Membership operators                       # EXTRA
t = (10, 20, 30)
print(20 in t)      # Output: True
print(50 not in t)  # Output: True

# 11. Tuple concatenation                         # EXTRA
a = (1, 2)
b = (3, 4)
print(a + b)  # Output: (1, 2, 3, 4)

# 12. Tuple repetition                            # EXTRA
t = (1, 2)
print(t * 2)  # Output: (1, 2, 1, 2)

# 13. Tuple unpacking                             # EXTRA
student = ("Rahul", 20, "CSE")
name, age, branch = student
print(name)   # Output: Rahul
print(age)    # Output: 20
print(branch) # Output: CSE

# 14. Iterating through a tuple                   # EXTRA
t = (10, 20, 30)
for item in t:
    print(item)  # Prints 10, 20, 30 on separate lines

# 15. Nested tuples                               # EXTRA
t = ((1, 2), (3, 4))
print(t[0])     # Output: (1, 2)
print(t[0][1])  # Output: 2

# 16. Converting a list into a tuple              # EXTRA
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)

# 17. Converting a tuple into a list              # EXTRA
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3]

# 18. Tuple immutability                          # EXTRA
t = (10, 20, 30)
# t[0] = 99  # TypeError: tuple elements cannot be reassigned

# 19. A tuple containing a mutable list           # EXTRA
t = (10, [20, 30])
t[1].append(40)
print(t)  # Output: (10, [20, 30, 40])