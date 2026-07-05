"""
Absolutely! Heaps (Priority Queues) are one of the most useful data structures 
for software engineering interviews. 
They're commonly used when a problem asks for the largest, smallest, or top K elements efficiently.

1. What is a Heap?
A Heap is a special type of Binary Tree that follows the heap property.

There are two types:

Min Heap
Max Heap

Min Heap

The smallest element is always at the root.

Example:
          2
        /   \
       5     8
      / \   /
     10 12 15

Notice:
2 < 5

2 < 8

5 < 10

5 < 12

8 < 15

Every parent is less than or equal to its children.

Max Heap
The largest element is always at the root.

          20
        /    \
      15      10
     / \      /
    8   7    5

Every parent is greater than or equal to its children.

Important

A Heap is NOT the same as a Binary Search Tree (BST).

Binary Search Tree
          10
         /  \
        5   20
       / \   /
      3   7 15

Heap
          2
        /   \
       5     8
      / \   /
     10 12 15

Only the parent-child relationship matters.

The left child isn't necessarily smaller than the right child.

How is a Heap Stored?
Unlike trees, heaps are usually stored in an array.

Heap:
          2
        /   \
       5     8
      / \   /
     10 12 15

Array:
heap = [2, 5, 8, 10, 12, 15]

The positions determine the tree structure.

For index i:
Left child  = 2*i + 1

Right child = 2*i + 2

Parent      = (i-1)//2

Example:
Index

0 1 2 3 4 5

Value

2 5 8 10 12 15

For index 1 (value = 5):
Left child

2*1+1 = 3

→ 10

Right child

2*1+2 = 4

→ 12

No pointers are needed!

Inserting into a Heap
Suppose we have:
          2
        /   \
       5     8
      /
     10

Insert 1.

Step 1

Add it at the end.
          2
        /   \
       5     8
      / \
     10  1

Oops!

The heap property is broken.

Bubble Up

Swap with parent.
          2
        /   \
       1     8
      / \
     10  5

Still wrong.

Swap again.
          1
        /   \
       2     8
      / \
     10  5

Done.

Removing the Minimum (Min Heap)
Suppose:
          1
        /   \
       2     8
      / \
     10  5

Remove the root.

Move the last element to the top.
          5
        /   \
       2     8
      /
     10

Oops!

Now 5 > 2.

Bubble Down
Swap with the smaller child.
          2
        /   \
       5     8
      /
     10

Heap restored.

Python Heap
Python provides the heapq module.

It implements a Min Heap.

Create a Heap
"""

import heapq

nums = [5, 1, 8, 3]

heapq.heapify(nums)

print(nums)

"""
Output:
[1, 3, 8, 5]

Notice the array isn't fully sorted. It only satisfies the heap property.

Insert
"""

import heapq

heap = [1, 3, 8]

heapq.heappush(heap, 2)

print(heap)

"""
Output:
[1, 2, 8, 3]

The heap property is maintained automatically.

Remove the Smallest
"""
smallest = heapq.heappop(heap)

print(smallest)

"""
Output:
1

Peek
print(heap[0])

Output:
2
The smallest element is always at index 0.

Time Complexity
| Operation              | Complexity |
| ---------------------- | ---------- |
| Peek smallest/largest  | O(1)       |
| Insert                 | O(log n)   |
| Remove root            | O(log n)   |
| Build heap (`heapify`) | O(n)       |

Example 1: K Smallest Numbers
Given:
nums = [8, 2, 10, 5, 1]

Find the 3 smallest numbers.

One approach:
Find the 3 smallest numbers.

One approach:
"""

import heapq

nums = [8, 2, 10, 5, 1]
heapq.heapify(nums)

for _ in range(3):
    print(heapq.heappop(nums))

"""
Output:
1
2
5

Example 2: Top K Largest Elements
Problem:
nums = [3, 2, 1, 5, 6, 4]

k = 2

Answer:
6

5

Python makes this easy:
"""
import heapq

nums = [3, 2, 1, 5, 6, 4]

print(heapq.nlargest(2, nums))

"""
Output:
[6, 5]

Min Heap vs Max Heap

Python only provides a Min Heap.

To simulate a Max Heap, store negative values.
"""

import heapq

nums = [5, 1, 8]

max_heap = []

for n in nums:
    heapq.heappush(max_heap, -n)

print(-heapq.heappop(max_heap))

"""
Output:
8

Because:
-8 < -5 < -1
the smallest negative value corresponds to the largest original value.

When Should You Think "Heap"?

Interview clues include:

"Top K largest/smallest"
"Kth largest/smallest"
"Continuously get the minimum or maximum"
"Merge multiple sorted lists"
"Task scheduling"
"Find the next item with the highest priority"

For example:

Find the 10 largest files → Heap
Always process the earliest event first → Min Heap
Show the top 5 highest scores → Max Heap

Heap vs Other Data Structures
| Data Structure     | Best For                                          |
| ------------------ | ------------------------------------------------- |
| Array              | Random access by index                            |
| Linked List        | Fast insert/delete at known positions             |
| Hash Map           | Fast key-value lookups                            |
| Binary Search Tree | Ordered searching and traversal                   |
| Heap               | Quickly accessing/removing the minimum or maximum |

Interview Roadmap

At this point, you've learned most of the foundational data structures and algorithm patterns:

✅ Arrays & Strings
✅ Linked Lists
✅ Hash Maps
✅ Two Pointers & Sliding Window
✅ Binary Search
✅ Trees & Binary Trees
✅ Graphs (BFS & DFS)
✅ Heaps / Priority Queues

The next topics I'd recommend are:

Recursion – understanding how functions call themselves.
Backtracking – solving puzzles like permutations, subsets, and Sudoku.
Dynamic Programming (DP) – optimizing recursive problems by storing intermediate results.

These are among the most common advanced topics in software engineering interviews. 
Once you're comfortable with them, you'll have covered the core concepts 
tested across most major tech companies.
"""





