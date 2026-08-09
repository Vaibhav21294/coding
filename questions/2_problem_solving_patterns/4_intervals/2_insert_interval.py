"""
Category
Data Structure: Array
Problem-Solving Pattern: Intervals ⭐⭐⭐

The problem is to insert a new interval into an already sorted list of non-overlapping intervals, merging if necessary.

Example
intervals = [[1,3],[6,9]]
newInterval = [2,5]

[2,5] overlaps with [1,3], so merge them:

[[1,5],[6,9]]
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []

        for i in range(len(intervals)):

            # Current interval is completely before new interval
            if intervals[i][1] < newInterval[0]:
                result.append(intervals[i])

            # Current interval is completely after new interval
            elif intervals[i][0] > newInterval[1]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result

            # Overlapping
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        result.append(newInterval)

        return result

"""
Complexity

Because we don't sort:

Time: O(n)

Space: O(n) for the result.
"""

