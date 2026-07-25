"""
This is one of the most important BFS problems for interviews.

In fact:

Maximum Depth (recursive) → DFS
Binary Tree Level Order Traversal → BFS

Interviewers often ask these two back-to-back to see if you know when to use DFS vs. BFS.

Problem Statement

Given the root of a binary tree, return the values of the nodes level by level.

Example:

        3
       / \
      9   20
         /  \
        15   7

Output:

[
    [3],
    [9, 20],
    [15, 7]
]

Notice that each inner list contains one level.

Why DFS is not the best choice

Suppose we use DFS.

DFS visits:

3
↓
9
↑
20
↓
15
↑
7

Result:

3,9,20,15,7

But the question wants:

Level 1

3

Level 2

9 20

Level 3

15 7

That is exactly what Breadth First Search (BFS) does.

BFS uses a Queue

A queue works as:

First In

↓

First Out

Just like people standing in a line.

Algorithm
Put the root into the queue.
While the queue is not empty:
Find how many nodes are currently in the queue.
Those nodes belong to the current level.
Process exactly those nodes.
Add their children to the queue.
Repeat.

Python Code
"""

from collections import deque

class Solution:
    def levelOrder(self, root):

        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:

            level = []
            level_size = len(queue)

            for _ in range(level_size):

                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result

"""
Dry Run

Tree:

        3
       / \
      9   20
         /  \
        15   7

Initially:

Queue

[3]

Result

[]
Iteration 1

Queue size:

1

Meaning:

There is 1 node at this level.

Process it.

Remove:

3

Level becomes:

[3]

Add children:

9

20

Queue:

[9,20]

Result:

[
   [3]
]

Space Complexity

The queue can contain an entire level.

Worst case:

        1
      /   \
     2     3
    / \   / \
   4  5  6   7

The last level has:

4 nodes

In a balanced tree, the last level contains about N/2 nodes.

So the queue may store:

O(N)

nodes.

Therefore:

Space = O(N)

Complexity Summary
| Complexity | Value    |
| ---------- | -------- |
| **Time**   | **O(N)** |
| **Space**  | **O(N)** |

DFS vs BFS
| Problem                           | Best Approach                    |
| --------------------------------- | -------------------------------- |
| Maximum Depth                     | DFS (Recursion)                  |
| Same Tree                         | DFS                              |
| Invert Binary Tree                | DFS                              |
| Binary Tree Level Order Traversal | **BFS**                          |
| Minimum Depth                     | Usually BFS                      |
| Right Side View                   | BFS (or DFS with level tracking) |

Interview Explanation

"Since the problem asks for nodes level by level, I use Breadth-First Search. 
I maintain a queue of nodes to visit. At the beginning of each iteration, 
I record the current queue size, which represents the number of nodes in the current level. 
I process exactly those nodes, add their children to the queue, and then append the collected values to the result. 
Each node is visited once, giving a time complexity of O(N) and a space complexity of O(N)."

A tip for recognizing BFS tree problems

If the problem mentions any of these phrases, think BFS with a queue:

Level order
Level by level
Nearest
Shortest path (in an unweighted graph)
Minimum number of steps
Distance from the root
"""