"""
3Sum is one of the most common interview problems 
because it combines Arrays, Sorting, and Two Pointers.

Problem Statement

Given an integer array nums, return all unique triplets [a, b, c] such that:

a + b + c = 0

The solution must not contain duplicate triplets.

Example
Input:
nums = [-1,0,1,2,-1,-4]

Output:
[
  [-1,-1,2],
  [-1,0,1]
]

Brute Force Idea

Try every possible combination of 3 numbers.

If their sum is 0, add them to the answer (avoiding duplicates).

Brute Force Code
"""
class Solution:
    def threeSum(self, nums):
        result = []

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):

                    if nums[i] + nums[j] + nums[k] == 0:

                        triplet = sorted([nums[i], nums[j], nums[k]])

                        if triplet not in result:
                            result.append(triplet)

        return result

"""
Time Complexity (Brute Force)

Three nested loops:

O(N³)

Checking:

triplet not in result

can make it even slower in practice, 
but interviewers usually summarize the brute-force approach as:

O(N³)

Space Complexity

Ignoring the output:

O(1)

(If you include the output, it depends on how many valid triplets exist.)

Optimized Idea

Instead of fixing all three numbers, fix only one number.

Then solve the remaining problem using Two Pointers.

Algorithm
Sort the array.
Pick one number (i).
Use:
left = i + 1
right = n - 1
Calculate:
total = nums[i] + nums[left] + nums[right]
If total == 0 → found a triplet.
If total < 0 → move left right.
If total > 0 → move right left.

Python Solution
"""

class Solution:
    def threeSum(self, nums):

        nums.sort()
        result = []

        n = len(nums)

        for i in range(n - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:

                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result

"""
Complexity Summary
Approach	Time	Space
Brute Force	O(N³)	O(1)
Sort + Two Pointers	O(N²)	O(1)
"""