"""
Problem

Given an integer array nums and an integer k, return the k most frequent elements.

Example
nums = [1,1,1,2,2,3]
k = 2

Output:
[1,2]

Frequency:

1 → 3 times
2 → 2 times
3 → 1 time

The two most frequent are:

[1,2]
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        pairs = list(hashmap.items())

        sorted_pairs = sorted(pairs, key=lambda x:x[1], reverse=True)

        result = []

        for i in range(k):
            result.append(sorted_pairs[i][0])

        return result

"""
Time = O(n log n)
Space: O(n)
"""