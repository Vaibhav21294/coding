"""
Two Sum is probably the #1 most asked coding interview problem. 
It teaches the fundamental use of a Hash Map.

Problem Statement

Given an array of integers nums and an integer target, return the indices of the two numbers 
such that they add up to target.

You may assume:

Exactly one solution exists.
You may not use the same element twice.

Example
Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]

Explanation:

2 + 7 = 9

The indices are:

2 -> index 0
7 -> index 1

Return:

[0, 1]

Brute Force Solution

Compare every number with every other number.
"""
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

"""
Dry Run
nums = [2,7,11,15]
target = 9
i = 0

    j = 1

    2 + 7 = 9 ✅

Return [0,1]

Time Complexity

Outer loop:

n

Inner loop:

n

Total:

O(n²)

Space Complexity

No extra data structure.

O(1)

Optimized Solution (Hash Map)

Instead of searching the entire array every time:

Ask this question:

"If my current number is x, what number do I need to reach the target?"

That number is called the complement.

Suppose

Current number = 7

Target = 9

Need:

9 - 7 = 2

So we ask:

"Have I already seen 2?"

A hash map can answer that in O(1) time.

Algorithm

For every number:

Compute the complement.
Check if the complement is already in the hash map.
If yes, return the indices.
Otherwise, store the current number and its index.

Python Solution
"""

def two_sum(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[nums[i]] = i

"""
Time Complexity

We iterate through the array once.

n elements

Each hash map operation (in, lookup, insert) takes O(1) on average.

Total Time Complexity
O(n)

Space Complexity

In the worst case, every element is stored in the hash map.

O(n)

Brute Force vs Optimized
| Approach    | Time     | Space    |
| ----------- | -------- | -------- |
| Brute Force | O(n²)    | O(1)     |
| Hash Map    | **O(n)** | **O(n)** |

Interview Explanation (30 seconds)

If the interviewer asks, "How did you optimize it?", you can say:

"The brute-force solution compares every pair of elements, which takes O(n²) time. 
To optimize it, I use a hash map that stores each number along with its index as I iterate through the array. 
For every number, I calculate its complement (target - current_number) and check whether it has already been seen. 
Since hash map lookups are O(1) on average, the entire algorithm runs in O(n) time with O(n) extra space."

This explanation demonstrates both your understanding of the algorithm and your ability to discuss its complexity clearly.
"""
