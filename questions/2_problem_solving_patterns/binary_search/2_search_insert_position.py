"""
Problem

Given a sorted array and a target, return:

The index if the target exists.
Otherwise, the index where it should be inserted to keep the array sorted.

Example 1:

nums = [1,3,5,6]
target = 5

Output = 2

Example 2:

nums = [1,3,5,6]
target = 2

Output = 1

Example 3:

nums = [1,3,5,6]
target = 7

Output = 4
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return left

"""
Complexity

Each iteration removes half of the remaining search space.

Time
O(log n)
Space

Only three variables are used:

left
right
mid

So:

O(1)
"""