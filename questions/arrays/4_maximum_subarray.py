"""
Maximum Subarray (LeetCode 53) is one of the most famous interview questions because it teaches Kadane's Algorithm.

The key insight is that you don't need to check every possible subarray.

Problem Statement

Given an integer array nums, find the contiguous subarray with the largest sum.

Return that sum.

Example:

nums = [-2,1,-3,4,-1,2,1,-5,4]

Output:

6

Because:

[4, -1, 2, 1]

Sum:

4 - 1 + 2 + 1 = 6

Brute Force

Generate every possible subarray.

Example:

nums = [1,2,3]

Subarrays are:

[1]
[1,2]
[1,2,3]

[2]
[2,3]

[3]

Compute every sum.

Keep the maximum.

Brute Force (time limit exceeds)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        max_value = float("-inf")

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                current_sum = sum(nums[i:j+1])
                max_value = max(max_value, current_sum)
        return max_value
    
class Solution:
    def maxSubArray(self, nums):

        maximum = float("-inf")

        for i in range(len(nums)):

            current_sum = 0

            for j in range(i, len(nums)):

                current_sum += nums[j]
                maximum = max(maximum, current_sum)

        return maximum

"""
Time Complexity

Outer loop:

N

Inner loop:

N

Total:

O(N²)
Space Complexity
O(1)

Optimal Solution (Kadane's Algorithm)

This is the important interview solution.

Algorithm

Keep two variables:

current_sum
maximum_sum

For every number:

current_sum = max(num, current_sum + num)

Meaning:

Choose the better option:

Start a new subarray from this number.
Extend the previous subarray.

Then update:

maximum_sum = max(maximum_sum, current_sum)

Python Code
"""

class Solution:
    def maxSubArray(self, nums):

        current_sum = nums[0]
        maximum_sum = nums[0]

        for i in range(1, len(nums)):

            current_sum = max(nums[i], current_sum + nums[i])

            maximum_sum = max(maximum_sum, current_sum)

        return maximum_sum

"""
Time Complexity

We visit each element exactly once.

O(N)
Space Complexity

We only use two variables:

current_sum
maximum_sum
O(1)

Complexity Summary
| Approach           | Time      | Space    |
| ------------------ | --------- | -------- |
| Brute Force        | **O(N²)** | **O(1)** |
| Kadane's Algorithm | **O(N)**  | **O(1)** |

Interview Thought Process

When you see:

Maximum sum
Contiguous subarray
Largest running total

Think:

"Can I decide at each position whether it's better to continue the previous subarray or start a new one?"

That question leads directly to Kadane's algorithm, which is the standard optimal solution for this problem.
"""