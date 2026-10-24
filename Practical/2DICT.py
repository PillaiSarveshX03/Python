
# 1. Creating a dictionary with three key-value pairs
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(dict1)
# Output: {'a': 1, 'b': 2, 'c': 3}


# 2. Accessing the value of a key
print(dict1['a'])
# Output: 1


# 3. Adding a new key-value pair
dict1['d'] = 4
print(dict1)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# 4. Updating the value of an existing key
dict1['a'] = 100
print(dict1)
# Output: {'a': 100, 'b': 2, 'c': 3, 'd': 4}


# 5. Deleting a key from the dictionary
dict1.pop('b')
print(dict1)
# Output: {'a': 100, 'c': 3, 'd': 4}


# 6. Getting all keys of a dictionary
print(dict1.keys())
# Output: dict_keys(['a', 'c', 'd'])


# 7. Getting all values of a dictionary
print(dict1.values())
# Output: dict_values([100, 3, 4])


# 8. Getting all key-value pairs
print(dict1.items())
# Output: dict_items([('a', 100), ('c', 3), ('d', 4)])


# 9. Finding the length of a dictionary
print(len(dict1))
# Output: 3


# 10. Checking whether a key exists
print('a' in dict1)
# Output: True


# ==================== EXTRA TOPICS ====================

# 11. Accessing a value safely using get()  # EXTRA
print(dict1.get('z'))
# Output: None (key 'z' does not exist)

# 12. Removing a key using del                 # EXTRA
del dict1['c']
print(dict1)
# Output: {'a': 100, 'd': 4}

# 13. Adding multiple key-value pairs using update()  # EXTRA
dict1.update({'e': 5, 'f': 6})
print(dict1)
# Output: {'a': 100, 'd': 4, 'e': 5, 'f': 6}

# 14. Iterating through dictionary keys          # EXTRA
for key in dict1:
    print(key)

# 15. Iterating through key-value pairs          # EXTRA
for key, value in dict1.items():
    print(key, value)

# 16. Creating a dictionary using dict()         # EXTRA
dict2 = dict(x=10, y=20)
print(dict2)
# Output: {'x': 10, 'y': 20}

# 17. Creating a dictionary using comprehension  # EXTRA
squares = {n: n*n for n in range(1, 4)}
print(squares)
# Output: {1: 1, 2: 4, 3: 9}

# 18. Creating an empty dictionary               # EXTRA
empty_dict = {}
print(empty_dict)
# Output: {}

# 19. Checking whether a value exists             # EXTRA
print(100 in dict1.values())
# Output: True

# 20. Clearing all dictionary entries             # EXTRA
dict1.clear()
print(dict1)
# Output: {}
