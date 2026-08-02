"""
Balanced Binary Tree (LeetCode 110)

Category
Data Structure: Tree (Binary Tree)
Traversal Technique: DFS (Recursion)

Problem Statement

Given the root of a binary tree, determine if it is height-balanced.

A binary tree is balanced if, for every node:

|height(left subtree) - height(right subtree)| <= 1

Return:

True if the tree is balanced.
False otherwise.
Example 1

Balanced
        3
       / \
      9  20
         / \
        15  7

Output:

True

Example 2

Not Balanced
        1
       /
      2
     /
    3

Output:

False

At node 1:

Left Height = 2
Right Height = 0

Difference = 2

Not balanced.
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):

            if not node:
                return 0

            left = dfs(node.left)
            if left == -1:
                return -1

            right = dfs(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return dfs(root) != -1

"""
Complexity
Time

Every node is visited exactly once.

Time: O(n)

Space

Recursion stack:

Balanced tree: O(log n)
Skewed tree: O(n)
"""