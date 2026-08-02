"""
Problem Statement

Given the root of a binary tree, return the diameter of the tree.

The diameter is the length of the longest path between any two nodes.

Important: The path does not have to pass through the root.

The answer is measured in edges, not nodes.

Example
        1
       / \
      2   3
     / \
    4   5

Longest path:

4 → 2 → 1 → 3

Number of edges:

3

Output:

3

Brute Force
Idea

For every node:

Compute the height of the left subtree.
Compute the height of the right subtree.
Diameter through this node:
leftHeight + rightHeight
Repeat for every node.

Complexity

Every node recomputes heights.

Time: O(n²)

Space: O(h)

Optimal Solution

This is very similar to Balanced Binary Tree.

The only difference is:

Instead of returning -1, we keep updating the maximum diameter.

Key Idea

For every node:

Compute

Left height
Right height

The longest path passing through this node is:

leftHeight + rightHeight

Update the answer.

Then return the height:

1 + max(leftHeight, rightHeight)
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0

        def dfs(node):
            nonlocal diameter

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        dfs(root)

        return diameter

"""
Dry Run

Tree:

        1
       / \
      2   3
     / \
    4   5
dfs(4)
left = 0
right = 0

diameter = max(0,0)

return height = 1
dfs(5)
left = 0
right = 0

diameter = 0

return 1
dfs(2)

Children returned:

left = 1
right = 1

Diameter through node 2:

1 + 1 = 2

Update:

diameter = 2

Return height:

2
dfs(3)
left = 0
right = 0

return 1
dfs(1)

Children returned:

left = 2
right = 1

Diameter through root:

2 + 1 = 3

Update:

diameter = 3

Return height:

3

Finished.

Answer:

3
DFS Call Tree
dfs(1)
│
├── dfs(2)
│   │
│   ├── dfs(4)
│   │   └── return 1
│   │
│   ├── dfs(5)
│   │   └── return 1
│   │
│   ├── diameter = max(0,1+1)=2
│   └── return 2
│
├── dfs(3)
│   └── return 1
│
├── diameter = max(2,2+1)=3
└── return 3

Complexity
Time

Every node is visited exactly once.

Time: O(n)

Space

Recursion stack:

Balanced tree: O(log n)
Skewed tree: O(n)

Connection to Balanced Binary Tree

These two problems have almost the same DFS structure.

The key insight is the same in both:

The recursive function returns the height to the parent.
While computing that height, you also compute some extra information:
Balanced Binary Tree: whether the subtree is balanced.
Diameter of Binary Tree: the longest path seen so far.

Connection to Balanced Binary Tree

These two problems have almost the same DFS structure.
"""

# Balanced Binary Tree
left = dfs(node.left)
right = dfs(node.right)

# Check balance
if abs(left - right) > 1:
    return -1

return 1 + max(left, right)

# Diameter of Binary Tree
left = dfs(node.left)
right = dfs(node.right)

# Update answer
diameter = max(diameter, left + right)

return 1 + max(left, right)
