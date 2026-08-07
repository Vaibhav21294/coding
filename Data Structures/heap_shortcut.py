"""
A simple introduction with an example:

A heap is a special tree-based data structure that helps us quickly find the smallest element (in a min-heap) or the largest element (in a max-heap). 
In Python, heapq provides a min-heap, where the smallest value is always kept at the first position (heap[0]).

Example:
"""
import heapq

heap = []

heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
"""
The heap internally looks like:

        10
       /  \
     30    20

Python stores it as:

[10, 30, 20]

Notice:

10 is always at the top because it is the smallest value.
The list is not fully sorted ([10,20,30] would be sorted).
We can quickly get the smallest value:

heap[0]

Output:

10

If we remove the smallest value:

heapq.heappop(heap)

It removes 10, and the heap adjusts itself:

       20
      /
    30

So in one sentence:

A heap is like a smart priority queue where the most important element (smallest in a min-heap) is always easily available.

For your Meeting Rooms II problem, the "important element" is the earliest meeting end time, 
because that tells us which room becomes available first.
"""