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
Interviewers often ask you to visit every node in a tree.
There are three main depth-first traversal orders.

1. Preorder
Order:
Root

Left

Right

Example:
          10
         /  \
        5    20
       / \   /
      3   7 15

Visit:
10

5

3

7

20

15

Python:
"""

def preorder(node):
    if node is None:
        return

    print(node.value)

    preorder(node.left)

    preorder(node.right)

"""
2. Inorder
Order:
Left

Root

Right

Order:
Left

Root

Right

Visit:
3

5

7

10

15

20

Python:
"""

def inorder(node):
    if node is None:
        return

    inorder(node.left)

    print(node.value)

    inorder(node.right)

"""
Important: For a Binary Search Tree, an inorder traversal prints the values in sorted order.

3. Postorder
Order:
Left

Right

Root

Visit:
3

7

5

15

20

10

Python:
"""

def postorder(node):
    if node is None:
        return

    postorder(node.left)

    postorder(node.right)

    print(node.value)

"""
Time Complexity
Each traversal visits every node exactly once.
| Operation | Time |
| --------- | ---- |
| Preorder  | O(n) |
| Inorder   | O(n) |
| Postorder | O(n) |
where n is the number of nodes.

Tree vs Binary Tree
| Tree                                                       | Binary Tree                                                               |
| ---------------------------------------------------------- | ------------------------------------------------------------------------- |
| A node can have any number of children.                    | A node can have at most two children.                                     |
| Children are not necessarily ordered.                      | Children are explicitly `left` and `right`.                               |
| Used for folder structures, organization charts, XML/HTML. | Used for searching, expression trees, heaps, and many interview problems. |

Interview Example
Consider this binary tree:
          8
         / \
        3   10
       / \    \
      1   6    14
         / \   /
        4   7 13

Can you answer these?

Root: 8
Leaf nodes: 1, 4, 7, 13
Parent of 6: 3
Left child of 8: 3
Right child of 10: 14
Height (longest path in edges): 3

Being comfortable identifying these properties is just as important as writing code.

Where Trees Are Used

You'll encounter trees in many real-world systems:

📁 File systems (folders and subfolders)
🌐 HTML/DOM in web browsers
🏢 Organization charts
📚 Database indexes
🔍 Search engines
🧮 Expression evaluators (e.g., parsing 3 + (4 * 5))

What to Learn Next
What to Learn Next

For interview preparation, I recommend this order:

Trees (understand the terminology)
Binary Trees (structure and traversals)
Binary Search Trees (BSTs) (search, insert, delete)
Breadth-First Search (Level Order Traversal)
Common Binary Tree interview problems (height, diameter, lowest common ancestor, invert tree, etc.)

Since you've already learned arrays, linked lists, hash maps, two pointers, 
sliding window, and binary search, 
Binary Search Trees are the perfect next topic 
because they combine the ideas of trees and efficient searching.
"""
