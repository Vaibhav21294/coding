# Here’s a simple example of a HashSet data structure in Python

# Using Python’s built-in set

# Create a hash set
fruits = {"apple", "banana", "cherry"}

# Add elements
fruits.add("mango")
print("After adding mango:", fruits)

# Remove an element
fruits.remove("banana")
print("After removing banana:", fruits)

# Check membership
print("Is apple present?", "apple" in fruits)   # True

# Iterate over elements
for fruit in fruits:
    print(fruit)

"""
After adding mango: {'apple', 'cherry', 'mango', 'banana'}
After removing banana: {'apple', 'cherry', 'mango'}
Is apple present? True
apple
cherry
mango
"""

"""
Explanation
A HashSet stores unique elements only — duplicates are automatically ignored.
It uses a hash table internally, so lookups, insertions, and deletions are all O(1) on average.
Python’s set is effectively a HashSet implementation.
"""