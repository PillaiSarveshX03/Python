# 1. Creating an empty dictionary
my_dict = {}
print(my_dict)  # Output: {}

# 2. Creating a dictionary using key-value pairs
car = {"brand": "Tesla", "model": "Model 3", "year": 2024}
print(car)  # Output: {'brand': 'Tesla', 'model': 'Model 3', 'year': 2024}

# 3. Creating a dictionary using dict()
student = dict(name="Rahul", age=20, branch="CSE")
print(student)  # Output: {'name': 'Rahul', 'age': 20, 'branch': 'CSE'}

# 4. Accessing a value using its key
print(car["brand"])  # Output: Tesla

# 5. Accessing a missing key using get()
print(car.get("color"))  # Output: None (no error)
print(car.get("color", "Red"))  # Output: Red (default value)

# 6. Updating an existing key
profile = {"name": "Bob", "role": "Developer"}
profile["role"] = "Senior Developer"
print(profile)  # Role is updated

# 7. Adding a new key-value pair
profile["location"] = "Mumbai"
print(profile)  # Location is added

# 8. Viewing all keys
stock = {"apples": 10, "bananas": 5}
print(stock.keys())  # Output: dict_keys(['apples', 'bananas'])

# 9. Viewing all values
print(stock.values())  # Output: dict_values([10, 5])

# 10. Viewing all key-value pairs
print(stock.items())  # Output: dict_items([('apples', 10), ('bananas', 5)])

# 11. Iterating through a dictionary using items()
for fruit, quantity in stock.items():
    print(f"We have {quantity} {fruit}.")

# ==================== EXTRA TOPICS ====================

# 12. Checking whether a key exists                 # EXTRA
print("apples" in stock)  # Output: True
print("grapes" not in stock)  # Output: True

# 13. Finding the number of key-value pairs         # EXTRA
print(len(stock))  # Output: 2

# 14. Removing an item using pop()                  # EXTRA
stock = {"apples": 10, "bananas": 5}
removed = stock.pop("apples")
print(removed)  # Output: 10
print(stock)  # Output: {'bananas': 5}

# 15. Removing the last inserted item using popitem()  # EXTRA
stock = {"apples": 10, "bananas": 5}
print(stock.popitem())  # Output: ('bananas', 5)
print(stock)  # Output: {'apples': 10}

# 16. Removing all items using clear()               # EXTRA
stock.clear()
print(stock)  # Output: {}

# 17. Adding multiple key-value pairs using update() # EXTRA
student = {"name": "Rahul"}
student.update({"age": 20, "branch": "CSE"})
print(student)  # Output: {'name': 'Rahul', 'age': 20, 'branch': 'CSE'}

# 18. Setting a default value using setdefault()     # EXTRA
student = {"name": "Rahul"}
student.setdefault("age", 20)
student.setdefault("name", "Amit")  # Existing value remains unchanged
print(student)  # Output: {'name': 'Rahul', 'age': 20}

# 19. Creating a copy of a dictionary                # EXTRA
original = {"a": 1, "b": 2}
copied = original.copy()
print(copied)  # Output: {'a': 1, 'b': 2}

# 20. Looping through dictionary keys                # EXTRA
student = {"name": "Rahul", "age": 20}
for key in student:
    print(key)  # Prints each key

# 21. Looping through dictionary values              # EXTRA
for value in student.values():
    print(value)  # Prints each value

# 22. Dictionary with different data types           # EXTRA
data = {"name": "Rahul", "marks": [80, 90, 95], "passed": True}
print(data)

# 23. Nested dictionary                             # EXTRA
students = {
    "student1": {"name": "Rahul", "age": 20},
    "student2": {"name": "Priya", "age": 19}
}
print(students["student1"]["name"])  # Output: Rahul

# 24. Dictionary comprehension                      # EXTRA
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 25. Creating a dictionary from two lists           # EXTRA
keys = ["name", "age"]
values = ["Rahul", 20]
student = dict(zip(keys, values))
print(student)  # Output: {'name': 'Rahul', 'age': 20}

# 26. Handling a missing key                         # EXTRA
car = {"brand": "Tesla"}
# print(car["color"])  # KeyError: key does not exist
print(car.get("color", "Unknown"))  # Output: Unknown

# 27. Duplicate keys                                # EXTRA
data = {"a": 10, "b": 20, "a": 30}
print(data)  # Output: {'a': 30, 'b': 20}; last value wins

# 28. Case-sensitive keys                           # EXTRA
data = {"Name": "Rahul", "name": "Priya"}
print(data["Name"])  # Output: Rahul
print(data["name"])  # Output: Priya