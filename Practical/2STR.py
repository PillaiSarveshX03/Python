# 1. Creating a string
string1 = "Python"
print(string1)  # Output: Python

# 2. Accessing the first character
print(string1[0])  # Output: P

# 3. Slicing the first three characters
print(string1[:3])  # Output: Pyt

# 4. Converting to uppercase
print(string1.upper())  # Output: PYTHON

# 5. Converting to lowercase
print(string1.lower())  # Output: python

# 6. Replacing a character
print(string1.replace("P", "J"))  # Output: Jython

# 7. Joining a list of characters into a string
print("".join(["a", "b", "c"]))  # Output: abc

# 8. Splitting a string using spaces
print("Hello World".split())  # Output: ['Hello', 'World']

# 9. Counting occurrences of a character
print(string1.count("t"))  # Output: 1

# 10. Reversing a string using slicing
print(string1[::-1])  # Output: nohtyP


# ==================== EXTRA TOPICS ====================

# 11. Finding the length of a string             # EXTRA
print(len(string1))  # Output: 6

# 12. Accessing the last character               # EXTRA
print(string1[-1])  # Output: n

# 13. Finding the index of a character           # EXTRA
print(string1.find("t"))  # Output: 2

# 14. Checking whether a string starts with      # EXTRA
print(string1.startswith("Py"))  # Output: True

# 15. Checking whether a string ends with        # EXTRA
print(string1.endswith("on"))  # Output: True

# 16. Capitalizing the first character           # EXTRA
print("hello world".capitalize())  # Output: Hello world

# 17. Capitalizing the first letter of each word # EXTRA
print("hello world".title())  # Output: Hello World

# 18. Removing whitespace from both ends        # EXTRA
text = "  Python  "
print(text.strip())  # Output: Python

# 19. Splitting using a specific separator       # EXTRA
print("apple,banana,mango".split(","))  # Output: ['apple', 'banana', 'mango']

# 20. Checking whether a string contains only digits # EXTRA
print("12345".isdigit())  # Output: True

# 21. Checking whether a string contains only letters # EXTRA
print("Python".isalpha())  # Output: True

# 22. Checking whether a string is alphanumeric   # EXTRA
print("Python123".isalnum())  # Output: True

# 23. Repeating a string                          # EXTRA
print("Hi " * 3)  # Output: Hi Hi Hi

# 24. Concatenating strings                       # EXTRA
first = "Hello"
second = "World"
print(first + " " + second)  # Output: Hello World

# 25. Checking membership                        # EXTRA
print("Py" in string1)  # Output: True

# 26. Formatting a string using f-string          # EXTRA
name = "Rahul"
age = 20
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Rahul and I am 20 years old.

# 27. Swapping uppercase and lowercase           # EXTRA
print("PyThOn".swapcase())  # Output: pYtHoN

# 28. Replacing a word                            # EXTRA
print("I like Java".replace("Java", "Python"))
# Output: I like Python

# 29. Checking whether a string is lowercase      # EXTRA
print("python".islower())  # Output: True

# 30. Checking whether a string is uppercase      # EXTRA
print("PYTHON".isupper())  # Output: True