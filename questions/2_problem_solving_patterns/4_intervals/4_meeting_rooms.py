"""
Meeting Rooms is a very common interview question (Microsoft, Google, Amazon). It tests:

Sorting
Intervals
Greedy thinking

There are actually two popular versions:

Meeting Rooms I → Can one person attend all meetings?
Meeting Rooms II → How many rooms are required?

Let's start with Meeting Rooms I because it is the foundation.

"""

class Solution:
    def canAttendMeetings(self, intervals):

        intervals.sort()

        for i in range(1, len(intervals)):

            previous_end = intervals[i-1][1]
            current_start = intervals[i][0]

            if current_start < previous_end:
                return False

        return True

"""
Complexity

Sorting:

O(n log n)

Loop:

O(n)

Overall:

O(n log n)

Space:

O(1)

(if sorting in-place)
"""