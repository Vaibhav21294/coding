"""
Absolutely! Graphs are one of the last major data structures 
you should learn for software engineering interviews. Once you're comfortable with Trees, 
Graphs become much easier because a tree is actually a special type of graph.

1. What is a Graph?

A graph is a collection of vertices (nodes) connected by edges.

Example:
      A
     / \
    B---C
     \
      D

* Vertices (nodes): A, B, C, D
* Edges:
    * A-B
    * A-C
    * B-C
    * B-D

Unlike a tree:

* A graph can have cycles.
* A node can have many neighbors.
* There is no root.

Real-world examples

Graphs are everywhere:

🗺️ Google Maps (cities connected by roads)
👥 Social networks (people connected by friendships)
✈️ Flight routes
🌐 Internet pages connected by links
🧩 Dependencies between software packages

Tree vs Graph
| Tree                                    | Graph                            |
| --------------------------------------- | -------------------------------- |
| Has one root                            | No root required                 |
| No cycles                               | Cycles allowed                   |
| Exactly one path between nodes          | Multiple paths possible          |
| Every node (except root) has one parent | Nodes can connect to many others |

Example Tree:
      A
     / \
    B   C
   /
  D

Example Graph:
      A
     / \
    B---C
     \
      D

Notice the extra edge between B and C, creating a cycle.

Representing a Graph in Python
The most common representation is an Adjacency List.

Graph:
      A
     / \
    B---C
     \
      D

Python:
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B"],
    "D": ["B"]
}

Meaning:
A connects to B and C

B connects to A, C and D

...

Traversing a Graph
Just like trees, we often need to visit every node.

The two most important algorithms are:

DFS (Depth First Search)
BFS (Breadth First Search)

These appear in almost every interview.

DFS (Depth First Search)
Idea:

Go as deep as possible before coming back.

Think of exploring a maze.

Keep walking...

Keep walking...

Dead end?

Go back.

Try another path.

Example graph
      A
     / \
    B   C
   / \
  D   E

Start at A.

Step 1
Visit
A

Step 2
Go deeper
A

↓

B

Step 3
Go deeper
A

↓

B

↓

D

D has no new neighbors.

Backtrack.
A

↓

B

↓

E

Backtrack again.

Finally
A

↓

C

DFS Order
A

B

D

E

C

DFS using Recursion
"""

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": [],
    "D": [],
    "E": []
}

def dfs(node):
    print(node)

    for neighbor in graph[node]:
        dfs(neighbor)

dfs("A")

"""
Output
A
B
D
E
C

Why do we need a Visited Set?

Consider:
A ---- B
|      |
|      |
C ---- D

If you don't remember where you've been:
A

↓

B

↓

D

↓

C

↓

A

↓

B

↓

...

You'll loop forever.

Solution:
visited = set()

Improved DFS:
"""

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

visited = set()

def dfs(node):
    if node in visited:
        return

    visited.add(node)
    print(node)

    for neighbor in graph[node]:
        dfs(neighbor)

dfs("A")

"""
Time Complexity
O(V + E)

where

V = vertices
E = edges

BFS (Breadth First Search)
Idea:

Instead of going deep...

Visit neighbors first.

Think of ripples spreading in water.

Level 0

A

↓

Level 1

B C

↓

Level 2

D E

Example
      A
     / \
    B   C
   / \
  D   E

Visit
A

Then
B

C

Then
D

E

Order
A

B

C

D

E

Notice how it visits level by level.

BFS uses a Queue

Queue:
First In

↓

First Out

Example
Queue

[A]

Remove A.

Add neighbors.
[B C]

Remove B.
Add its neighbors.
[C D E]

Remove C.
[D E]

Continue.

BFS Python
"""

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": [],
    "D": [],
    "E": []
}

def bfs(start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

bfs("A")

"""
Output
A
B
C
D
E

DFS vs BFS
| DFS                                  | BFS                                            |
| ------------------------------------ | ---------------------------------------------- |
| Goes deep first                      | Goes level by level                            |
| Uses Stack (or recursion)            | Uses Queue                                     |
| Can use recursion                    | Usually iterative                              |
| May not find the shortest path       | Finds the shortest path in an unweighted graph |
| Good for exploring all possibilities | Good for minimum number of steps               |

Visual Comparison
Same graph
      A
     / \
    B   C
   / \
  D   E

DFS
A

↓

B

↓

D

↑

↓

E

↑

↓

C

Order
A B D E C

BFS
Level 0

A

↓

Level 1

B C

↓

Level 2

D E

Order
A B C D E

Common Interview Questions

DFS is commonly used for:

Number of islands
Detecting cycles
Maze solving
Backtracking
Connected components

BFS is commonly used for:

Shortest path in an unweighted graph
Word Ladder
Rotten Oranges
Level-order traversal of trees
Minimum number of moves/problems

Interview Tips

When reading a problem:

If you see "explore every possible path", "detect a cycle", or "visit all connected nodes", think DFS.
If you see "shortest path", "minimum number of steps", or "level by level", think BFS.

Where Graphs Fit in Your Interview Preparation

So far, you've covered:

✅ Arrays & Strings
✅ Linked Lists
✅ Hash Maps
✅ Two Pointers & Sliding Window
✅ Binary Search
✅ Trees & Binary Trees
✅ Graphs (DFS & BFS)

The next topics I'd recommend are:

Binary Search Trees (BSTs) – search, insert, delete
Heaps / Priority Queues – very common in interview problems involving "top K", scheduling, or merging
Recursion & Backtracking – subsets, permutations, N-Queens
Dynamic Programming – one of the most challenging but rewarding interview topics

By the time you finish these, you'll have covered the core data structures and algorithms 
asked in most software engineering interviews.
"""
