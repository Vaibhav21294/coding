"""
Invert Binary Tree (LeetCode 226)
Category
Data Structure: Tree (Binary Tree)
Traversal Technique: DFS (Recursion)

Problem Statement

Given the root of a binary tree, invert the tree and return its root.

Inverting a tree means swapping the left and right child of every node.

Example

Input:
        4
      /   \
     2     7
    / \   / \
   1   3 6   9

Output:
        4
      /   \
     7     2
    / \   / \
   9   6 3   1

Optimal Solution (DFS)
Idea

At every node:

Swap the left and right child.
Recursively invert the left subtree.
Recursively invert the right subtree.

Repeat until you reach None.
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

"""
Dry Run

Initial tree:

        4
      /   \
     2     7
dfs(4)

Swap children.

        4
      /   \
     7     2

Now recurse left and right.

dfs(7)

Before:

    7
   / \
  6   9

Swap.

    7
   / \
  9   6

Children are leaves.

Done.

dfs(2)

Before:

    2
   / \
  1   3

Swap.

    2
   / \
  3   1

Done.

Final tree:

        4
      /   \
     7     2
    / \   / \
   9   6 3   1

DFS Call Tree
dfs(4)
│
├── swap(4)
│
├── dfs(7)
│   │
│   ├── swap(7)
│   ├── dfs(9)
│   └── dfs(6)
│
└── dfs(2)
    │
    ├── swap(2)
    ├── dfs(3)
    └── dfs(1)

Complexity
Time

Every node is visited exactly once.

Time: O(n)

Space

The recursion stack depends on the tree height.

Balanced tree: O(log n)
Skewed tree: O(n)

Pattern to Remember

Most recursive tree problems follow this template:

def dfs(node):

    if not node:
        return

    # Do something with the current node

    dfs(node.left)
    dfs(node.right)

For Invert Binary Tree, the "do something" step is simply:

node.left, node.right = node.right, node.left
"""