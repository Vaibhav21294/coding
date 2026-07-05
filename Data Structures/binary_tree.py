"""
A Binary Tree is a special type of tree where every node can have at most two children.
They are usually called:

Left Child
Right Child
Example:
          10
         /  \
        5    20
       / \   /
      3   7 15
Notice:

10 has two children.
20 has one child.
3, 7, and 15 have no children.

Every node has 0, 1, or 2 children.

Python Representation
A common way to represent a binary tree is with a class:

"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
Create the tree:
"""

root = TreeNode(10)

root.left = TreeNode(5)
root.right = TreeNode(20)

root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

root.right.left = TreeNode(15)

"""
This creates:
          10
         /  \
        5    20
       / \   /
      3   7 15

Accessing Nodes
print(root.value)

Output:
10

print(root.left.value)
Output:
5

print(root.right.left.value)
15

Tree Traversals
"""
