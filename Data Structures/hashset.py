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
