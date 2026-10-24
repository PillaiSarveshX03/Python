# 1. Creating a set of integers
my_set = {1, 2, 3}
print(my_set)  # Output: {1, 2, 3}

# 2. Creating a set with mixed data types
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)  # Contains 1.0, "Hello", and (1, 2, 3)
# NOTE: Set element order is not guaranteed.

# 3. Removing duplicates using set()
raw_list = [1, 2, 2, 3, 3, 3]
cleaned_set = set(raw_list)
print(cleaned_set)  # Output: {1, 2, 3}

# 4. Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()
# NOTE: {} creates an empty dictionary, not a set.

# 5. Adding a single element using add()
skills = {"Python", "SQL"}
skills.add("Git")
print(skills)  # Contains Python, SQL, Git

# 6. Adding multiple elements using update()
skills.update(["AWS", "Docker"])
print(skills)  # Contains Python, SQL, Git, AWS, Docker

# 7. Removing an element using remove()
languages = {"Python", "Java", "C++"}
languages.remove("Java")
print(languages)  # Contains Python and C++

# 8. Removing an element safely using discard()
languages.discard("Ruby")
print(languages)  # No error if Ruby is absent

# 9. Removing and returning an arbitrary element using pop()
languages = {"Python", "Java", "C++"}
removed = languages.pop()
print(removed)    # One arbitrary element removed
print(languages)  # Remaining elements
 
# 10. Removing all elements using clear()
languages.clear()
print(languages)  # Output: set()


# ==================== MATHEMATICAL OPERATIONS ====================

setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

# 11. Union: elements from either set
print(setA | setB)  # Output: {1, 2, 3, 4, 5, 6}
print(setA.union(setB))  # Same result

# 12. Intersection: common elements
print(setA & setB)  # Output: {3, 4}
print(setA.intersection(setB))  # Same result

# 13. Difference: elements in A but not in B
print(setA - setB)  # Output: {1, 2}
print(setA.difference(setB))  # Same result

# 14. Symmetric difference: elements in either set, but not both
print(setA ^ setB)  # Output: {1, 2, 5, 6}
print(setA.symmetric_difference(setB))  # Same result


# ==================== SUBSET AND SUPERSET ====================

# 15. Checking subset and superset relationships
small = {1, 2}
large = {1, 2, 3, 4}

print(small.issubset(large))    # Output: True
print(large.issuperset(small))  # Output: True

# 16. Checking whether sets have no common elements
print(small.isdisjoint(large))  # Output: False





# ==================== EXTRA TOPICS ====================

# 17. Checking membership                       # EXTRA
numbers = {10, 20, 30}
print(20 in numbers)      # Output: True
print(50 not in numbers)  # Output: True

# 18. Finding the number of elements              # EXTRA
print(len(numbers))  # Output: 3

# 19. Looping through a set                       # EXTRA
for item in numbers:
    print(item)  # Prints each element; order is not guaranteed

# 20. Checking whether a set is a subset using an operator  # EXTRA
print({1, 2} <= {1, 2, 3})  # Output: True

# 21. Checking whether a set is a superset using an operator  # EXTRA
print({1, 2, 3} >= {1, 2})  # Output: True

# 22. Copying a set                               # EXTRA
original = {1, 2, 3}
copied = original.copy()
print(copied)  # Output: {1, 2, 3}

# 23. Creating a set using set comprehension      # EXTRA
squares = {x**2 for x in range(1, 6)}
print(squares)  # Contains 1, 4, 9, 16, 25

# 24. Converting a set into a list                 # EXTRA
numbers = {10, 20, 30}
number_list = list(numbers)
print(number_list)  # A list containing the set elements; order may vary

# 25. Creating a frozenset                        # EXTRA
fixed_set = frozenset([1, 2, 3])
print(fixed_set)  # frozenset({1, 2, 3})
# A frozenset is immutable; its elements cannot be added or removed.

# 26. Demonstrating that duplicate elements are ignored  # EXTRA
numbers = {1, 2, 2, 3, 3}
print(numbers)  # Contains only 1, 2, 3

# 27. Demonstrating invalid indexing               # EXTRA
# print(numbers[0])  # TypeError: sets do not support indexing

# 28. Demonstrating invalid mutable elements       # EXTRA
# invalid_set = {[1, 2, 3]}  # TypeError: lists are unhashable