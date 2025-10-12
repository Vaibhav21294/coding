# A Binary Tree is a hierarchical data structure in which each node 
# has at most two children — a left and a right child.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Create a simple binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Traverse the tree (Preorder)
def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

preorder(root)  # Output: 1 2 4 5 3

"""
This tree looks like:
      1
     / \
    2   3
   / \
  4   5
Each node has up to two children, which is the key property of a binary tree.
"""

