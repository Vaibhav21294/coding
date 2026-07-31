"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false

Category
Data Structure: Tree (Binary Tree)
Traversal Technique: DFS (Recursion)
"""

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left)
            and
            self.isSameTree(p.right, q.right)
        )

"""
Dry Run

Trees:

    1          1
   / \        / \
  2   3      2   3

Call:

isSameTree(1,1)

Values match.

Now compare left.

isSameTree(2,2)

Values match.

Compare children.

None vs None → True
None vs None → True

Left subtree returns:

True

Now compare right.

isSameTree(3,3)

Again:

None vs None → True
None vs None → True

Right subtree returns:

True

Final answer:

True AND True

↓

True

Complexity

Let n be the number of nodes.

Time

Every node is visited exactly once.

Time: O(n)

Space

The recursion stack depends on the height of the tree.

Balanced tree: O(log n)
Worst case (skewed tree): O(n)
"""