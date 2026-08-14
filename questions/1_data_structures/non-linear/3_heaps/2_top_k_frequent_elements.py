"""
Question

Given an integer array nums and an integer k, return the k most frequent elements.

You may return the answer in any order.

Example
Input:
nums = [1,1,1,2,2,3]
k = 2

Output:
[1,2]

Because:

1 → 3 times
2 → 2 times
3 → 1 time

So the top 2 frequent elements are [1,2].
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        heap = []

        for num, frequency in hashmap.items():
            heapq.heappush(heap, (frequency, num))

            if len(heap) > k:
               heapq.heappop(heap)     
                
        ans = []

        for frequency, num in heap:
            ans.append(num)
        
        return ans

"""
Complexity

Let:

n = number of elements in nums
m = number of unique elements
k = number we want

Frequency counting:

O(n)

Heap operations for m unique elements:

O(m log k)

Since m ≤ n:

Time
O(n + m log k)

Often simplified to:

O(n log k)

Space

HashMap:

O(m)

Heap:

O(k)

Overall:

O(n)

because m ≤ n.
"""