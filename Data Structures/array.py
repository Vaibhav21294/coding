# In Python, arrays can be represented using lists (most common) or the array module.

# Example using Python list (dynamic array)
# Creating an array (list in Python)
numbers = [10, 20, 30, 40, 50]

# Accessing elements
print("First element:", numbers[0]) # 10
print("Last element:", numbers[-1]) # 50

# Modifying an element
numbers[2] = 99
print("After modification:", numbers)  # [10, 20, 99, 40, 50]

# Adding a new element
numbers.append(60)
print("After append:", numbers)  # [10, 20, 99, 40, 50, 60]

# Example using Python array module (fixed type)
import array

# Creating an integer array
arr = array.array('i', [1, 2, 3, 4, 5])

# Accessing elements
print("First element:", arr[0])  # 1

# Adding a new element
arr.append(6)

print("After append:", arr)  # array('i', [1, 2, 3, 4, 5, 6])

# Removing an element
arr.remove(3)
print("After removal:", arr)  # array('i', [1, 2, 4, 5, 6])

# In interviews, Python lists are usually considered arrays because they behave like dynamic arrays (can grow/shrink).