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
"""