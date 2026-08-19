'''
Points

1. Create
2. Add, Remove
3. Iterate

'''

'''
| Operation        | Array / List     | String        | HashSet       | HashMap                 |
| ---------------- | ---------------- | ------------- | ------------- | ----------------------- |
| **Create**       | `nums = []`      | `s = ""`      | `s = set()`   | `d = {}`                |
| **Add**          | `nums.append(x)` | ❌ immutable   | `s.add(x)`    | `d[key] = value`        |
| **Remove**       | `nums.pop(i)`    | ❌ immutable   | `s.remove(x)` | `d.pop(key)`            |
| **Access**       | `nums[i]`        | `s[i]`        | ❌ no index    | `d[key]`                |
| **Iterate**      | `for x in nums:` | `for c in s:` | `for x in s:` | `for k,v in d.items():` |
| **Check exists** | `x in nums`      | `x in s`      | `x in s`      | `key in d`              |
| **Length**       | `len(nums)`      | `len(s)`      | `len(s)`      | `len(d)`                |
'''

# 1. Arrays

nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

for i in range(len(nums)):
    print(nums[i])

"""
Syntax VariationsThe function accepts up to three integer arguments:

pythonrange(stop)
range(start, stop)
range(start, stop, step)

How Arguments Workstart (Optional): 
The first number in the sequence. 
Defaults to 0.stop (Required): The number where the sequence ends. 
The value is exclusive, meaning the sequence stops right before this number.step 
(Optional): The increment value between each number. Defaults to 1.
"""

for i in range(5):
    print(i, end=" ")
# Output: 0 1 2 3 4

for i in range(2, 6):
    print(i, end=" ")
# Output: 2 3 4 5

for i in range(0, 10, 2):
    print(i, end=" ")
# Output: 0 2 4 6 8

# 4. Reverse CountingTo count downwards, use a larger start value and a negative
for i in range(5, 0, -1):
    print(i, end=" ")
# Output: 5 4 3 2 1

nums = []                 # create

nums[i]                   # access
nums[-1]                  # last

for num in nums:          # iterate
    ...

for i, num in enumerate(nums):
    ...

nums.append(x)            # add
nums.pop()                # remove last
nums.pop(i)               # remove index

x in nums                 # search

len(nums)                 # size

nums[i:j]                 # slice

nums.sort()               # sort
nums.reverse()            # reverse

######################################################################################

# 2. Strings

name = "Vaibhav"

for char in name:
    print(char)

"""
V
a
i
b
h
a
v
"""

s = ""                         # create

s[i]                          # access
s[-1]                         # last

for char in s:                # iterate
    ...

for i, char in enumerate(s):
    ...

len(s)                        # size

char in s                     # search

s[i:j]                        # slice
s[::-1]                       # reverse

s.lower()
s.upper()

char.isalpha()
char.isdigit()
char.isalnum()

s.split()                     # string → list
"".join(chars)                # list → string

list(s)                       # string → list

######################################################################################

# 3. Hashsets

s = set()

s.add(x)          # add
s.remove(x)       # remove (error if absent)
s.discard(x)      # remove (no error if absent)

x in s            # check existence

for x in s:       # iterate
    ...

len(s)            # size

######################################################################################

# 4. Hashmaps

d = {}                         # create

d[key]                        # access

d[key] = value                # add / update

d.get(key)                    # get value
d.get(key, 0)                 # get with default

key in d                      # check if key exists

d[key] += 1                   # increment

d.pop(key)                    # remove

len(d)                        # size

for key in d:                 # iterate keys
    ...

for key, value in d.items():  # iterate key + value
    ...

for value in d.values():      # iterate values
    ...

d.keys()                      # all keys
d.values()                    # all values
d.items()                     # key-value pairs



