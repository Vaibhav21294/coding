"""
Difference between linear and non linear data structures

This is actually very simple.

The difference is how the data is connected.

| Linear Data Structure                     | Non-Linear Data Structure                |
| ----------------------------------------- | ---------------------------------------- |
| Data is arranged in a **single sequence** | Data branches in **multiple directions** |
| One element leads to the next             | One element can lead to many others      |
| Easy to traverse from start to end        | Requires DFS/BFS or similar traversal    |

Linear Data Structures
Imagine people standing in a line.

A → B → C → D

There is only one path.

Examples:

Array
String
Linked List
Stack
Queue

For example, an array:

[10, 20, 30, 40]

You go

10 → 20 → 30 → 40

Only one direction.

Non-Linear Data Structures

Imagine a family tree.
        A
      /   \
     B     C
    / \     \
   D   E     F

There isn't just one path.

From A you can go to:

B
C

From B you can go to:

D
E

This is why we need algorithms like:

DFS
BFS

Examples
Linear
Array

[1,2,3,4,5]
1 → 2 → 3 → 4 → 5

Non-Linear
Tree

        10
       /  \
      5    20
          /  \
        15    30

Node 20 has two children.

Graph
A ----- B
| \     |
|  \    |
C ----- D

Easy Way to Remember
Linear = One Road 🚗
Home ---- School ---- Office ---- Mall

Only one road.

Non-Linear = Road Network 🗺️
            Home
           /    \
      School   Office
         |      /   \
      Mall   Gym   Park
Multiple roads.

For Interviews
| Topic       | Linear? | Non-Linear? |
| ----------- | ------- | ----------- |
| Array       | ✅       | ❌           |
| String      | ✅       | ❌           |
| Linked List | ✅       | ❌           |
| Stack       | ✅       | ❌           |
| Queue       | ✅       | ❌           |
| Heap        | ✅*      | ❌           |
| Tree        | ❌       | ✅           |
| Graph       | ❌       | ✅           |
| Trie        | ❌       | ✅           |

Note: A Heap is technically implemented as a binary tree, 
so in computer science it is a non-linear data structure. 
However, in interview preparation it's often grouped with arrays 
because it's usually stored in an array and many heap problems feel array-based. 
That's why you may see it classified either way.

My Interview Rule

For interview preparation, I would remember:

Linear = You move forward one element at a time.
Non-Linear = You can move to multiple children/neighbors, so you usually need DFS or BFS.

That's enough to classify almost every problem you'll encounter.
"""