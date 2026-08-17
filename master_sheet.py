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

######################################################################################

