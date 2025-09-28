# Example using Python list (dynamic array)
# Creating an array (list in Python)
numbers = [10, 20, 30, 40, 50]

# Accessing elements
print("First element:", numbers[0])   # 10
print("Last element:", numbers[-1])  # 50

# Modifying an element
numbers[2] = 99
print("After modification:", numbers)  # [10, 20, 99, 40, 50]

# Adding a new element
numbers.append(60)
print("After append:", numbers)  # [10, 20, 99, 40, 50, 60]
