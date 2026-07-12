"""
Merge Intervals is an excellent next problem 
because it's much simpler and introduces a very common interview pattern.

Problem Statement

You are given an array of intervals where:

intervals = [[start, end], ...]

Merge all overlapping intervals.

Return the merged intervals.

Example 1
intervals = [[1,3],[2,6],[8,10],[15,18]]

Output:

[[1,6],[8,10],[15,18]]

Why?

[1-----3]
     [2--------6]

↓

[1------------6]

The intervals overlap, so they become one interval.

Example 2
intervals = [[1,4],[4,5]]

Output:

[[1,5]]

They touch at 4, so they're considered overlapping.

Key Observation

Two intervals overlap if:

current_start <= previous_end

Example:

Previous interval:

[1------5]

Current interval:

      [4------8]

Since

4 <= 5

they overlap.

If instead:

Previous:

[1----3]

Current:

       [5----7]

Since

5 > 3

they do not overlap.

Step 1: Sort

Always sort by the start value.

Example:

[[8,10],[1,3],[15,18],[2,6]]

After sorting:

[[1,3],[2,6],[8,10],[15,18]]

Why?

Because we only need to compare each interval with the one we've already merged.

Algorithm
1. Sort intervals.
2. Put the first interval into the result.
3. For each remaining interval:
    If it overlaps with the last interval in the result:
        Merge them.
    Otherwise:
        Add it to the result.

Python Code
"""

class Solution:
    def merge(self, intervals):

        intervals.sort()

        result = [intervals[0]]

        for start, end in intervals[1:]:

            last_end = result[-1][1]

            if start <= last_end:
                result[-1][1] = max(last_end, end)
            else:
                result.append([start, end])

        return result
    
"""
Time Complexity
Step 1: Sort

Sorting N intervals:

O(N log N)
Step 2: Traverse

One loop:

O(N)

Total:

O(N log N)

Sorting dominates.

Space Complexity

Ignoring the output array:

O(1)

If you include the returned result:

O(N)

Interview Thought Process

When you see:

Intervals
Overlapping ranges
Meeting schedules
Time ranges

Think:

Sort by the start value.
Compare the current interval with the last merged interval.
If they overlap, extend the end.
Otherwise, start a new interval.

This "sort first, then scan once" pattern appears in many interval problems.

Where this fits in your interview roadmap

You've now covered:

✅ Arrays & Hash Maps
✅ Two Pointers / Sliding Window
✅ Binary Search
✅ Trees
✅ Basic Graphs (Number of Islands)
✅ Intervals (Merge Intervals)

After this, the natural progression is:

Insert Interval (slightly harder interval problem)
Meeting Rooms / Meeting Rooms II (interval scheduling)
Return to Course Schedule, where you'll already be comfortable with DFS and graph traversal.
"""