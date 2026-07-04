# A string is a data structure used to store a sequence of characters (letters, numbers, symbols, spaces, etc.).

# In Python, strings are enclosed in quotes:

name = "Vaibhav"

# Key Property
# Strings in Python are immutable, which means you cannot change individual characters after the string is created.

s = "Hello"

# This will cause an error
s[0] = "J"

# Basic String Operations
# 1. Access Characters (Indexing)
s = "Python"

print(s[0])   # P
print(s[2])   # t
print(s[-1])  # n

# 2. Slicing
# Extract part of a string.
s = "Python"

print(s[0:3])   # Pyt
print(s[2:])    # thon
print(s[:4])    # Pyth

# 3. Concatenation
# Combine strings using +.
first = "Hello"
second = "World"

result = first + " " + second

print(result)
# Hello World

# 4. Repetition
s = "Hi "

print(s * 3)
# Hi Hi Hi

# 5. Length
s = "Python"

print(len(s))
# 6

# 6. Search
# Check if a substring exists
s = "Hello World"

print("World" in s)
# True

# Find index
s = "Hello World"

print(s.find("World"))
# 6

# 7. Replace
s = "I like Java"

new_s = s.replace("Java", "Python")

print(new_s)
# I like Python

# 8. Convert Case
s = "PyThOn"

print(s.lower())  # python
print(s.upper())  # PYTHON

# 9. Split
s = "apple,banana,mango"

fruits = s.split(",")

print(fruits)
# ['apple', 'banana', 'mango']

# 10. Join
# Convert a list into a string.
words = ["I", "love", "Python"]

sentence = " ".join(words)

print(sentence)
# I love Python

# 11. Strip Spaces
s = "   hello   "

print(s.strip())
# hello

# Common Interview Operations
# Reverse a String
s = "Python"

reversed_s = s[::-1]

print(reversed_s)
# nohtyP

# Count Characters
s = "banana"

print(s.count("a"))
# 3

# Check Palindrome
s = "madam"

print(s == s[::-1])
# True

# Iterate Through String
s = "Python"

for ch in s:
    print(ch)

# Time Complexity Summary
""""
| Operation           | Complexity |
| ------------------- | ---------- |
| Access by index     | O(1)       |
| Length              | O(1)       |
| Search substring    | O(n)       |
| Slice               | O(k)       |
| Concatenation (`+`) | O(n + m)   |
| Reverse             | O(n)       |
| Replace             | O(n)       |
"""

"""
For software engineering interviews (including companies like Google and Meta), the most important string topics are:

Two pointers on strings
String reversal
Palindrome checking
Anagrams
Frequency counting using dictionaries
Sliding window on strings
Pattern matching problems

Mastering these covers a large percentage of common string interview questions.
"""
