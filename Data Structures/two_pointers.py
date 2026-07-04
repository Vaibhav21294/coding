"""
Absolutely. Two Pointers and Sliding Window are among the most frequently tested techniques in software engineering interviews 
(especially at companies like Google, Meta, Amazon, and Microsoft). They aren't separate data structures—they are problem-solving patterns.
"""

"""
1. Two Pointers
What is it?

Instead of using one index to traverse an array, we use two indices (pointers).

The pointers may:

Move towards each other
Move in the same direction
Move at different speeds

This often reduces an O(n²) solution to O(n).
"""

"""
Example 1: Two Sum in a Sorted Array

Problem

Given a sorted array:
"""

nums = [1, 2, 4, 7, 11, 15]
target = 15

"""Find two numbers that add up to 15.

# Expected
4 + 11 = 15
"""

"""
Brute Force
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [nums[i], nums[j]]
"""

"""
Time Complexity:
O(n²)
"""

"""
Two Pointer Solution

Start

Left                 Right

1 2 4 7 11 15
^               ^

Current sum:
1 + 15 = 16

Too large.
Move right pointer left.
1 2 4 7 11 15
^           ^

1 + 11 = 12

Too small.
Move left pointer.

1 2 4 7 11 15
  ^         ^

2 + 11 = 13
Too small.

Move left.
1 2 4 7 11 15
    ^       ^

4 + 11 = 15    
Found!
"""

def two_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current = nums[left] + nums[right]

        if current == target:
            return [nums[left], nums[right]]

        elif current < target:
            left += 1

        else:
            right -= 1

    return None

# Output
print(two_sum([1,2,4,7,11,15],15))

# [4, 11]

# Time
# O(n)

"""
Example 2: Reverse an Array

arr = [1,2,3,4,5]

Two pointers:
1 2 3 4 5
L       R

Swap
5 2 3 4 1
  L   R

Swap
5 4 3 2 1
"""

def reverse(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return arr
