"""
The Merge Sorted Array problem asks you to merge two sorted arrays into nums1 in-place.

Problem
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output:

[1,2,2,3,5,6]

Example: Merge Sorted Array (LeetCode 88)
1. Brute Force
Idea

Copy all elements from nums2 into the empty spaces of nums1, then sort the entire array.

Algorithm
Copy every element of nums2 into nums1.
Sort nums1.

Code
"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1[m + i] = nums2[i]

        nums1.sort()

"""
Complexity
Time: O((m + n) log(m + n))
Copying: O(n)
Sorting: O((m+n) log(m+n))
Space: O(1) (Python's list.sort() sorts in place, though it may use a small amount of auxiliary memory internally.)
"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

"""
Complexity
Time: O(m + n)
Space: O(1) (in-place)
"""
