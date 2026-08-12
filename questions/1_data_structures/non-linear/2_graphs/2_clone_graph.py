"""
Clone Graph is one of the most common graph questions in interviews. It tests:

Graph traversal (DFS or BFS)
Hash Map
Recursion (or Queue)
Handling cycles

Difficulty: Medium

Problem Statement

Given a node in a connected graph, create a deep copy of the graph.

Example:

Original

    1
   / \
  2---3
   \
    4

The cloned graph should be completely separate in memory:

Cloned

    1'
   / \
 2'---3'
  \
   4'

Changing the clone should not affect the original graph.

Node Definition
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

Each node has

value
list of neighbors

Why is this tricky?

Suppose we start with

1

Create

1'

Now copy neighbor

2

Create

2'

Now from 2 we go back to

1

Should we create another node?

No!

Otherwise

1

would become

1' 1''

which is wrong.

We need to remember:

"Have I already cloned this node?"

Solution

Use a Hash Map.

The hash map stores

original_node -> cloned_node

Example

{
 1 : 1',
 2 : 2',
 3 : 3'
}

DFS Walkthrough

Original graph

1 ----- 2
|       |
|       |
4 ----- 3

Start

clone(1)

HashMap

{}

Visit 1

Create

1'

Store

{
1 : 1'
}

Visit neighbor 2

Create

2'

Store

{
1 : 1'
2 : 2'
}

2 has neighbor 1

Already cloned.

Instead of creating again

Just return

1'

2 has neighbor 1

Already cloned.

Instead of creating again

Just return

1'

Continue

3

↓

4

Eventually

{
1 : 1'
2 : 2'
3 : 3'
4 : 4'
}

Done.
"""

class Solution:
    def cloneGraph(self, node):

        if not node:
            return None

        old_to_new = {}

        def dfs(node):

            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)

            old_to_new[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)

"""
Time Complexity

Each node visited once.

Each edge visited once.

O(V + E)

where

V = vertices (nodes)
E = edges
Space Complexity

HashMap

O(V)

Recursion stack

O(V)

Overall

O(V)
"""