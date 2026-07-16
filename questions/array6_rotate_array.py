"""
Let's solve LeetCode 189: Rotate Array the way we'll do all interview problems.

Problem

Given an integer array nums, rotate the array to the right by k steps.

Example
Input:
nums = [1,2,3,4,5,6,7]
k = 3

Output:
[5,6,7,1,2,3,4]

1. Brute Force
Idea

Rotate the array one step to the right, k times.

For one rotation:

[1,2,3,4]

↓

[4,1,2,3]

Repeat this k times.

Algorithm

For each rotation:

Store the last element.
Shift every element one position to the right.
Put the last element at index 0.

Code
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)

        for _ in range(k):
            last = nums[n - 1]

            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]

            nums[0] = last

"""
Complexity
Time: O(n × k)
Space: O(1)

Very slow when k is large.

2. Better Solution
Idea

Use an extra array.

Every element at index i moves to

(i + k) % n

Example:

nums = [1,2,3,4,5]
k = 2

0 → 2
1 → 3
2 → 4
3 → 0
4 → 1

Code
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        result = [0] * n

        for i in range(n):
            result[(i + k) % n] = nums[i]

        for i in range(n):
            nums[i] = result[i]

"""
Complexity
Time: O(n)
Space: O(n)
"""