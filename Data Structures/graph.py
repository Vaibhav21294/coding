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
"""