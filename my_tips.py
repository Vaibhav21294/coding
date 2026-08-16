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

7. Process:
Brute Force
Dry run
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

9. str = "abc"

for i in range(len(str)):
    for j in range(i+1, len(str)+1):
        print(str[i:j])

a
ab
abc
b
bc
c

10. break vs continue
for num in [1, 2, 3, 4, 5]:
    if num == 3:
        break
    print(num)

1
2

for num in [1, 2, 3, 4, 5]:
    if num == 3:
        continue
    print(num)

1
2
4
5

11. array.sort() # in place
sorted.array()

12. for start, end in intervals[1:]

13.
pairs = list(hashmap.items())

sorted_pairs = sorted(pairs, key=lambda x:x[1], reverse=True)

14. # Getting last digit for a num
while n > 0:
    digit = n % 10
    total += digit * digit
    n = n // 10

15: Iterate over string elements
s = "Vaibhav"
for i in range(len(s)):
    print(s[i])

16.
.isalnum()

.lower()

17. stack
LIFO
stack.eppend()
stack.pop()

18.
result.extend(...)

extend() adds each item from another list into the current list.

Example:

result = [[1,5]]

result.extend([[10,12], [15,18]])

Now:

result

is:

[[1,5], [10,12], [15,18]]

19.
intervals = [[1,2],[2,3],[3,4],[1,3]]

intervals.sort(key=lambda x:x[1])

20. 
Tuple: (frequency, num) stores two related values together as one object. 
Python compares tuples from left to right, so (frequency, num) is primarily ordered by frequency.

21.
Python compares tuples from left to right.

So:

(1,3)
(2,2)
(3,1)

Python primarily looks at the first number.

(1,3)  → first value = 1
(2,2)  → first value = 2
(3,1)  → first value = 3

Therefore:

(1,3)

is the smallest tuple.

So:

heapq.heappop(heap)

removes:

(1,3)

because 1 is the smallest frequency.

22.
for num, frequency in hashmap.items():

23. 
n // 2

means integer division.

For example:

8 // 2 = 4
5 // 2 = 2

24. 
Check if number is even:    
if n % 2 == 0:
"""