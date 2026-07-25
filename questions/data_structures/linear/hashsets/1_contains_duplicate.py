"""
Problem

Given an integer array nums, return True if any value appears at least twice. Otherwise, return False.

Example
Input: [1,2,3,1]

Output: True
Input: [1,2,3,4]

Output: False
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for num in nums:
            if num in hashmap:
                return True

            hashmap[num] = 1

        return False
    
"""
Still:

Time: O(n)
Space: O(n)

Even better with a set

Since you don't need counts, use a set:
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False

"""
Complexity
Time: O(n)
Space: O(n)

Ask yourself: "Do I actually need the count, or do I only need to know if I've seen this before?"

Need counts? → Dictionary (dict)
Just need existence? → Set (set)
"""