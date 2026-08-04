"""
Category
Data Structure: Array
Problem-Solving Pattern: Binary Search ⭐

Problem Statement

Suppose an array is sorted in ascending order and then rotated.

Find the minimum element.

You must solve it in O(log n) time.

Example 1
Input:
nums = [3,4,5,1,2]

Output:
1
Example 2
Input:
nums = [4,5,6,7,0,1,2]

Output:
0
Example 3
Input:
nums = [1,2,3,4]

Output:
1

(Not rotated)

Optimal Solution (Binary Search)
Key Observation

A rotated sorted array has two sorted halves.

Example:

4 5 6 7 | 0 1 2

The minimum is where the rotation happened.

We can use Binary Search to find it.
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

"""
Complexity
Time: O(log n)
Space: O(1)

Interview Tip

When you see:

Sorted array
Rotated
O(log n) required

your first thought should be:

Binary Search
"""
