"""
Excellent. Maximum Depth of Binary Tree is probably the #1 recursion interview problem. 
Once you understand this, many tree problems become much easier.

Problem Statement

Given the root of a binary tree, return its maximum depth.

The depth is the number of nodes along the longest path from the root to a leaf.

Example:
        3
       / \
      9   20
         /  \
        15   7

Maximum depth is:

3

Because the longest path is:

3 → 20 → 15

(or 3 → 20 → 7)

Brute Force Thought Process

When you are at a node, ask:

"What is the maximum depth of my left subtree?"

and

"What is the maximum depth of my right subtree?"

Whichever is larger determines the answer.

Then simply add 1 for the current node.

This naturally leads to recursion.  

Recursive Formula

For every node:

Depth(node)

=

1 + max(Depth(left), Depth(right))

The only base case is:

if node is None:
    return 0

Python Solution
"""

class Solution:
    def maxDepth(self, root):

        if root is None:
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return 1 + max(leftDepth, rightDepth)
    
"""
Notice how short the solution is—because recursion is doing the work for us.

Dry Run

Tree:

        3
       / \
      9   20
         /  \
        15   7

Let's start at the root.

Step 1
maxDepth(3)

We don't know the answer yet.

So we ask:

leftDepth = maxDepth(9)

rightDepth = maxDepth(20)

Step 2

Go to node 9.

maxDepth(9)

Again:

leftDepth = maxDepth(None)

rightDepth = maxDepth(None)

Both return:

0

So:

return 1 + max(0,0)

= 1

Node 9 has depth 1.

Step 3

Now go to node 20.

maxDepth(20)

Need:

maxDepth(15)

maxDepth(7)
Step 4

Node 15

Both children are None.

return 1

Step 5

Node 7

Same.

return 1
Step 6

Back to node 20.

Now we know:

leftDepth = 1

rightDepth = 1

Return:

1 + max(1,1)

=

2

Step 7

Back to node 3.

Now we know:

leftDepth = 1

rightDepth = 2

Return:

1 + max(1,2)

=

3

Final answer:

3

Visualizing the Returns
            3
           / \
          9   20
             /  \
           15    7

Node 15 returns:

1

Node 7 returns:

1

Node 20 returns:

1 + max(1,1)

=

2

Node 9 returns:

1

Root returns:

1 + max(1,2)

=

3

Notice something important:

The recursion works from the bottom of the tree upward.

Why Recursion Works

Every node only needs two pieces of information:

Depth of left subtree
Depth of right subtree

Once it has both, its own answer is immediate.

That's exactly what recursion provides.

Time Complexity

Ask yourself:

How many times is each node visited?

Each node is visited exactly once.

If there are N nodes:

Time = O(N)

Space Complexity

This is where many people get confused.

We don't create any arrays or dictionaries.

However, recursion uses the call stack.

Suppose the tree is:

1
 \
  2
   \
    3
     \
      4

The recursive calls look like:

maxDepth(1)

↓

maxDepth(2)

↓

maxDepth(3)

↓

maxDepth(4)

There are 4 function calls on the stack.

So the space depends on the height of the tree, denoted by H.

Space = O(H)

est Case (Balanced Tree)
        1
      /   \
     2     3
    / \   / \
   4  5  6   7

Height:

log N

Space:

O(log N)
Worst Case (Skewed Tree)
1
 \
  2
   \
    3
     \
      4

Height:

N

Space:

O(N)
Complexity Summary
Complexity	Value
Time	O(N)
Space	O(H) (O(log N) balanced, O(N) worst case)
Interview Explanation

"For each node, I recursively compute the maximum depth of its left and right subtrees. The depth of the current node is one plus the larger of those two depths. Since every node is visited exactly once, the time complexity is O(N). The recursion stack uses space proportional to the tree height, so the space complexity is O(H)."

A pattern to remember

Many binary tree recursion problems follow this template:

def dfs(node):

    if node is None:
        return ...

    left = dfs(node.left)
    right = dfs(node.right)

    return combine(left, right)

The only thing that changes from problem to problem is the base case and the combine step.

For Maximum Depth, the combine step is:

return 1 + max(left, right)

You'll see this same recursion pattern again in problems like Diameter of Binary Tree, Balanced Binary Tree, and Path Sum.

is the solution DFS?

Yes! 🎯

The recursive solution is Depth-First Search (DFS).

In fact, most recursive tree solutions are DFS.

Why is it DFS?

Look at the code:

def maxDepth(root):

    if root is None:
        return 0

    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return 1 + max(left, right)

Suppose the tree is:

        3
       / \
      9   20
         /  \
        15   7

The function visits nodes in this order:

3
↓
9
↓
None
↑
None
↑
3
↓
20
↓
15
↓
None
↑
None
↑
20
↓
7
↓
None
↑
None
↑
20
↑
3

Notice what it's doing:

It goes as deep as possible down one branch.
Only after reaching the bottom does it come back up.

That is exactly what Depth-First Search means.

Compare DFS and BFS
DFS (used here)
        3
       / \
      9   20
         /  \
        15   7

Visit order:

3 → 9 → back → 20 → 15 → back → 7

Go deep first.

BFS

Visit level by level:

Level 1:
3

Level 2:
9 20

Level 3:
15 7

Visit order:

3 → 9 → 20 → 15 → 7
There are actually 2 ways to solve Maximum Depth
Method 1: DFS (Recursion) ✅ Most common
def maxDepth(root):
    if root is None:
        return 0

    return 1 + max(maxDepth(root.left),
                   maxDepth(root.right))

Time:

O(N)

Space:

O(H)
Method 2: BFS (Queue)

Visit one level at a time.

Each time you finish a level:

depth += 1

When the queue becomes empty,

return depth

Also:

Time: O(N)

Space: O(N)

because the queue can hold an entire level of the tree.

Interview Tip

If an interviewer asks:

"Is this DFS or BFS?"

Look at the implementation:

Uses recursion or an explicit stack → DFS
Uses a queue and processes level by level → BFS
A quick rule to remember
Technique	Uses	Traversal
DFS	Recursion or Stack	Go deep into one branch first
BFS	Queue	Visit level by level

So yes, the solution for Maximum Depth of Binary Tree that we wrote is a recursive DFS solution. 
In interviews, if you present that solution, it's perfectly fine to say:

"I'm solving this using Depth-First Search (DFS) with recursion."

Complexity Summary
| Complexity | Value                                             |
| ---------- | ------------------------------------------------- |
| **Time**   | **O(N)**                                          |
| **Space**  | **O(H)** (`O(log N)` balanced, `O(N)` worst case) |

Interview Explanation

"For each node, I recursively compute the maximum depth of its left and right subtrees. 
The depth of the current node is one plus the larger of those two depths. 
Since every node is visited exactly once, the time complexity is O(N). 
The recursion stack uses space proportional to the tree height, so the space complexity is O(H)."

A pattern to remember

Many binary tree recursion problems follow this template:

def dfs(node):

    if node is None:
        return ...

    left = dfs(node.left)
    right = dfs(node.right)

    return combine(left, right)

The only thing that changes from problem to problem is the base case and the combine step.

For Maximum Depth, the combine step is:

return 1 + max(left, right)

You'll see this same recursion pattern again in problems like Diameter of Binary Tree, 
Balanced Binary Tree, and Path Sum.
"""

