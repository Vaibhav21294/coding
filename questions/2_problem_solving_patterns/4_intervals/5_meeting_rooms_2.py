"""
Meeting Rooms II (LeetCode / Premium)
Category
Data Structure: Array + Heap
Problem-Solving Pattern: Intervals ⭐⭐⭐

Problem Statement

You are given a list of meeting intervals.

intervals = [[start1,end1],[start2,end2],...]

Return the minimum number of meeting rooms required.

Example 1
Input:
[[0,30],[5,10],[15,20]]

Output:
2

Explanation:

Room 1: 0 -------- 30

Room 2:     5--10
                 15--20

Two rooms are needed.

Example 2
Input:
[[7,10],[2,4]]

Output:
1

The meetings don't overlap.

Brute Force
Idea

For every meeting:

Try placing it into every existing room.

If no room is available, create a new room.

Complexity
Time: O(n²)
Space: O(n)

Optimal Solution (Min Heap)
Key Idea

Sort meetings by start time.

Keep a min heap of ending times.

The smallest ending time is always at the top.

Why?

Suppose we've scheduled:

Meeting End Times

10
20
30

Heap:

10
20
30

The meeting ending at 10 finishes first.

When a new meeting starts:

Start = 12

Since

12 >= 10

that room becomes free.

We remove it from the heap.

Algorithm
Step 1

Sort by start time.

[0,30]
[5,10]
[15,20]

Step 2

Put the first meeting's end time into the heap.

Heap:
30
"""