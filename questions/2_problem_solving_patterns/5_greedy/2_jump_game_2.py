"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

Example
nums = [2, 3, 1, 1, 4]

index:  0  1  2  3  4
value:  2  3  1  1  4

nums = [2, 3, 1, 1, 4]

index:  0  1  2  3  4
value:  2  3  1  1  4

From index 0, we can jump:

0 → 1
0 → 2

We want the minimum number of jumps.

The answer is:

0 → 1 → 4

2 jumps
"""

class Solution:
    def jump(self, nums):
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):

            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps

"""
This is the standard greedy solution and runs in O(n) time and O(1) space.
"""