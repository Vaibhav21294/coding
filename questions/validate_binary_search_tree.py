"""
Excellent choice. Validate Binary Search Tree (BST) is one of the most important tree interview problems 
because it tests whether you truly understand what a BST is.

Problem Statement

Given the root of a binary tree, determine whether it is a valid Binary Search Tree (BST).

Return:

True if valid
False otherwise

What is a BST?

A Binary Search Tree follows these rules:

For every node:

All nodes in the left subtree must be smaller.
All nodes in the right subtree must be greater.

Example:
       5
      / \
     3   8
    / \ / \
   2  4 6  9

This is a valid BST.

Invalid Example
       5
      / \
     3   8
        /
       4

At first glance:

4 < 8 ✅

So it looks okay.

But remember:

4 is in the right subtree of 5.

Everything in the right subtree of 5 must be greater than 5.

Since:

4 < 5

This is not a BST.

This is the trick of the problem.

First Idea (Incorrect)

Many beginners write:

if root.left.val < root.val < root.right.val:
    return True

or recursively compare each node with its immediate children.

This does not work.

Why?

Consider:

       5
      / \
     3   8
        /
       4

At node 8:

4 < 8

Looks valid.

But 4 violates the rule imposed by node 5.

So checking only the parent is not enough.

Correct Idea

Each node must stay within an allowed range.

Initially:

(-∞, +∞)

The root can be anything.

Suppose the root is:

5

Now:

Left child must be in:

(-∞, 5)

Right child must be in:

(5, +∞)

Suppose left child is:

3

Its left child must be:

(-∞, 3)

Its right child must be:

(3, 5)

Notice something?

The upper limit 5 is still remembered.

That's the key.

Visual Example
           5
         /   \
        3     8
       / \
      2   4

Allowed ranges:

5

(-∞, +∞)

↓

3

(-∞, 5)

↓

2

(-∞, 3)

↓

4

(3, 5)

Every node has its own valid range.

"""

class Solution:

    def isValidBST(self, root):

        def dfs(node, low, high):

            if node is None:
                return True

            if not (low < node.val < high):
                return False

            return (
                dfs(node.left, low, node.val)
                and
                dfs(node.right, node.val, high)
            )

        return dfs(root, float("-inf"), float("inf"))

"""
Dry Run

Tree:

       5
      / \
     3   8
        /
       4

Start:

dfs(5, -∞, +∞)

Is:

-∞ < 5 < +∞

Yes.

Go left.

dfs(3, -∞, 5)

Is:

-∞ < 3 < 5

Yes.

Go right.

dfs(8, 5, +∞)

Is:

5 < 8 < +∞

Yes.

Go left.

dfs(4, 5, 8)

Allowed range:

(5,8)

Check:

5 < 4 < 8

False.

Return:

False

Entire answer becomes:

False

Why DFS?

Notice the recursion:

dfs(node.left, ...)
dfs(node.right, ...)

We keep going deep into one branch before returning.

That is Depth-First Search (DFS).

Time Complexity

Ask yourself:

How many times do we visit each node?

Exactly once.

If there are N nodes:

Time = O(N)

Space Complexity

We only use recursion.

The recursion depth equals the height of the tree.

Balanced tree:

O(log N)

Worst case (skewed tree):

O(N)

So:

Space = O(H)

Complexity Summary
| Complexity | Value    |
| ---------- | -------- |
| Time       | **O(N)** |
| Space      | **O(H)** |

Interview Thought Process

When you see this problem, think:

❌ Comparing only a node with its children is not enough.
✅ Every node must satisfy the constraints imposed by all of its ancestors.
✅ Pass a minimum and maximum allowed value down the recursion.
✅ This naturally leads to a DFS recursive solution.

A Tip to Remember

Think of every node carrying an invisible "permission slip" that says:

"Your value must stay between low and high."

Every recursive call updates those limits:

Going left: the current node becomes the new upper bound.
Going right: the current node becomes the new lower bound.

If any node violates its allowed range, the tree is not a valid BST. 
This "range checking" approach is the standard interview solution and 
is much more robust than comparing only parent and child values.
"""