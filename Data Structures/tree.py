"""
Absolutely. Trees are one of the most important data structures for software engineering interviews. 
Once you understand a general Tree, learning a Binary Tree, Binary Search Tree (BST), 
and later interview questions becomes much easier.

1. What is a Tree?
A Tree is a hierarchical data structure made up of nodes connected by edges.
Unlike arrays or linked lists, a tree branches into multiple paths.

Example:
            A
         /  |  \
        B   C   D
       / \      |
      E   F     G

Think of it like:

A family tree
A company's organizational chart
Your computer's folder structure

Each circle (A, B, C...) is called a node.

Each line connecting nodes is called an edge.

Terminology
Using the same tree
            A
         /  |  \
        B   C   D
       / \      |
      E   F     G

Root
The topmost node.
A

Parent
A node that has children.
Example:
A is parent of B,C,D

B is parent of E,F

Child
Nodes below a parent.
B is child of A

E is child of B

Leaf Node
A node with no children.
C

E

F

G

Subtree
The tree rooted at any node.

Subtree rooted at B:

    B
   / \
  E   F


"""

# Define a Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    # Add child node
    def add_child(self, child_node):
        self.children.append(child_node)

    # Display tree recursively
    def display(self, level=0):
        print(" " * 2 * level + f"- {self.data}")
        for child in self.children:
            child.display(level+1)

# Create a root node
root = Node("Electronics")

# Create child nodes
laptop = Node("Laptop")
phone = Node("Phone")
tv = Node("TV")

# Add children to root
root.add_child(laptop)
root.add_child(phone)
root.add_child(tv)

# Add sub-children
laptop.add_child(Node("MacBook"))
laptop.add_child(Node("Dell"))
phone.add_child(Node("iPhone"))
phone.add_child(Node("Samsung"))

# Display the tree
root.display()
