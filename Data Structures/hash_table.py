#Hash table

# Create a hash table (dictionary)
hash_table = {}

# Insert key–value pairs
hash_table["apple"] = 10
hash_table["banana"] = 20
hash_table["orange"] = 30

# Access a value by key
print("Price of banana:", hash_table["banana"])   # 20

# Update a value
hash_table["apple"] = 15
print("Updated apple price:", hash_table["apple"])  # 15

# Delete a key
del hash_table["orange"]
print("After deletion:", hash_table)  # {'apple': 15, 'banana': 20}

# Check if key exists
if "banana" in hash_table:
    print("Banana exists in table")

#Output
#Price of banana: 20
#Updated apple price: 15
#After deletion: {'apple': 15, 'banana': 20}
#Banana exists in table

