"""
My tips

1. Always do brute force first. Atleast I have one solution by now

2. Dry run data structure questions before implementing code

3. When you see code like this:
for i in range(n):
    for j in range(i + 1, n):
    
a quick mental shortcut is:

"I'm comparing every pair of elements exactly once."

The number of unique pairs in a collection of n items is:

n(n - 1) / 2

and that simplifies to O(n²).

4. visited = [False] * len(strs)

5. 
word = "cba"
sorted_word = sorted(word)
print(sorted_word) # ['a', 'b', 'c']
ans = "".join(sorted_word)
print(ans) # abc

6. 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        groups = defaultdict(list)

        for str in strs:
            key = "".join(sorted(str))
            groups[key].append(str)
        return list(groups.values())

7. Problem solving:
Brute Force
Optimal solution
Time complexity
Space complexity

8. In Python, a set is a built-in data type used to store an unordered collection of unique items.
# Creating a set with elements
fruits = {"apple", "banana", "cherry", "apple"} 
print(fruits)  # Output: {'banana', 'cherry', 'apple'} (Duplicates are removed!)

# Creating an empty set
# Note: {} creates an empty dictionary, so you must use set()
empty_set = set() 

# Converting a list to a set (useful for removing duplicates)
numbers_list = [1, 2, 2, 3, 4, 4]
unique_numbers = set(numbers_list)
print(unique_numbers)  # Output: {1, 2, 3, 4}

my_set = {1, 2, 3}

# Add a single item
my_set.add(4) # {1, 2, 3, 4}

# Add multiple items from any iterable
my_set.update([4, 5, 6]) # {1, 2, 3, 4, 5, 6}

# Remove an item (Raises KeyError if the item doesn't exist)
my_set.remove(3) 

# Discard an item (Does NOT raise an error if the item is missing)
my_set.discard(10) 

# Remove and return an arbitrary element
popped_item = my_set.pop() 

# Clear all items
my_set.clear() # set()

"""