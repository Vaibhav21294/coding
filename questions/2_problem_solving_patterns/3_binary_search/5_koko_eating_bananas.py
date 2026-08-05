"""
Category
Data Structure: Array
Problem-Solving Pattern: Binary Search on Answer ⭐⭐⭐

This is one of the most important Binary Search interview patterns.
"""

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        while left < right:

            mid = (left + right) // 2

            hours = 0

            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left

"""
Complexity

Let:

n = number of piles
m = maximum pile size

Binary Search runs:

O(log m)

Each iteration scans all piles:

O(n)

Overall:

Time: O(n log m)
Space: O(1)

Interview Tip

This problem introduces an extremely important pattern:

Binary Search on the Answer

You are not searching an array. Instead, you're searching for the smallest valid value in a range.

Whenever a problem asks for:

Minimum possible value
Maximum possible value
"Can we finish within X?"
"Can we achieve this limit?"

and the answer changes monotonically (once it becomes valid, it stays valid), think:

Binary Search on the Answer

Other famous problems using this pattern include:

Capacity to Ship Packages Within D Days
Split Array Largest Sum
Minimum Days to Make Bouquets
Smallest Divisor Given a Threshold

These all follow the same idea: guess an answer, check if it's valid, then binary search the range.
"""