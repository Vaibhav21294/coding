"""
Problem

Given an unsorted array of integers nums, return the length of the longest consecutive sequence.

The sequence elements do not need to be adjacent in the array.

Example
Input:  [100, 4, 200, 1, 3, 2]

Output: 4

Explanation:
1, 2, 3, 4
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        nums.sort()

        longest_sequence = 1
        result = 1

        left = 0
        right = 1

        while right<len(nums):
            diff = nums[right] - nums[left]
            if diff == 1:
                longest_sequence += 1
            elif diff == 0:
                right += 1
                left += 1
                continue 
            else:
                longest_sequence = 1
            result = max(longest_sequence, result)
            right += 1
            left += 1

        return result
    
"""
Time Complexity
Sorting: O(n log n)
While loop: O(n)

Overall:

O(n log n + n) = O(n log n)

✅ Correct.

Space Complexity

Ignoring Python's internal sorting implementation (which is the convention in interviews):

O(1)

3. Optimal Solution (Hash Set)
Algorithm
Put all numbers into a set.
For each number:
If num - 1 exists, skip it.
Otherwise start counting forward.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                length = 1

                while num + length in num_set:
                    length += 1

                longest = max(longest, length)

        return longest
    
"""
Complexity
Time: O(n)
Space: O(n)
"""