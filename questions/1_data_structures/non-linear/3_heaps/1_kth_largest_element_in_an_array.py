"""
Given an integer array nums and an integer k, return the kth largest element in the array.

The element is based on sorted order, not distinct values.

Example
Input:
nums = [3,2,1,5,6,4]
k = 2

Output:
5

Because sorted in descending order:

6, 5, 4, 3, 2, 1
    ↑
   2nd

Optimal Solution — Min Heap

Since we only need the k largest elements, we don't need to sort everything.

Keep a min heap of size k.

Idea

For:

nums = [3,2,1,5,6,4]
k = 2

Maintain only the 2 largest elements.

3 → [3]
2 → [2,3]
1 → [2,3]       ← remove 1
5 → [3,5]       ← remove 2
6 → [5,6]       ← remove 3
4 → [5,6]       ← 4 doesn't enter

At the end:

[5,6]
 ↑
min heap top

The smallest element among the top k elements is the kth largest.

Answer = 5.   
"""

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

"""
Time = O(n log k)

Space = O(k)

because the heap only holds k elements.
"""