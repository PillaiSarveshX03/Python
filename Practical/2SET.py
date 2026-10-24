# 1. Creating a set with five numbers
set1 = {1, 2, 3, 4, 5}
print(set1)  # Output: {1, 2, 3, 4, 5}

# 2. Adding an element to a set
set1.add(6)
print(set1)  # Contains {1, 2, 3, 4, 5, 6}

# 3. Removing an element from a set
set1.remove(3)
print(set1)  # Contains {1, 2, 4, 5, 6}

# 4. Performing union of two sets
print({1, 2, 3}.union({3, 4, 5}))
# Output: {1, 2, 3, 4, 5}

# 5. Performing intersection of two sets
print({1, 2, 3}.intersection({2, 3, 4}))
# Output: {2, 3}

# 6. Finding the difference between two sets
print({1, 2, 3}.difference({2, 3}))
# Output: {1}

# 7. Converting a list into a set
print(set([1, 2, 2, 3]))
# Output: {1, 2, 3} (duplicates removed)

# 8. Finding the length of a set
print(len(set1))  # Output: 5

# 9. Checking whether a value exists in a set
print(3 in set1)  # Output: False (3 was removed earlier)

# 10. Clearing all elements from a set
set1.clear()
print(set1)  # Output: set()


# ==================== EXTRA TOPICS ====================

# 11. Removing an element safely using discard()  # EXTRA
set2 = {1, 2, 3}
set2.discard(5)  # No error even though 5 is absent
print(set2)  # Output: {1, 2, 3}

# 12. Adding multiple elements using update()      # EXTRA
set2.update([4, 5, 6])
print(set2)  # Contains {1, 2, 3, 4, 5, 6}

# 13. Finding the symmetric difference             # EXTRA
print({1, 2, 3} ^ {3, 4, 5})
# Output: {1, 2, 4, 5}

# 14. Checking subset relationship                 # EXTRA
print({1, 2}.issubset({1, 2, 3}))  # Output: True

# 15. Checking superset relationship               # EXTRA
print({1, 2, 3}.issuperset({1, 2}))  # Output: True

# 16. Checking whether sets are disjoint            # EXTRA
print({1, 2}.isdisjoint({3, 4}))  # Output: True

# 17. Removing and returning an arbitrary element  # EXTRA
set3 = {10, 20, 30}
removed = set3.pop()
print(removed)  # One arbitrary element
print(set3)  # Remaining elements

# 18. Checking membership                          # EXTRA
print(2 in {1, 2, 3})  # Output: True

# 19. Creating an empty set                         # EXTRA
empty_set = set()
print(empty_set)  # Output: set()

# 20. Removing duplicates from a list              # EXTRA
numbers = [1, 1, 2, 2, 3, 3]
unique_numbers = set(numbers)
print(unique_numbers)  # Contains {1, 2, 3}