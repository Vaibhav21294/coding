"""
Excellent. LeetCode 78: Subsets is usually the first backtracking problem people learn. 
It teaches the core idea behind many other problems like Permutations, Combination Sum, and N-Queens.

We'll follow our interview format.

Problem

Given an array of unique integers, return all possible subsets.

Example:

nums = [1,2]

Output:

[
 [],
 [1],
 [2],
 [1,2]
]

Notice:

For n numbers, there are always

2ⁿ

subsets.
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]:

        result = []   # Stores all subsets
        subset = []   # Current subset being built

        def dfs(index):

            # Base case: processed every number
            if index == len(nums):
                result.append(subset.copy())   # Save a COPY
                return

            # Choice 1: Include current number
            subset.append(nums[index])
            dfs(index + 1)

            # Undo the choice (Backtrack)
            subset.pop()

            # Choice 2: Exclude current number
            dfs(index + 1)

        dfs(0)
        return result

"""
dfs(0), subset=[]
                        []
                     (dfs(0))
                    /          \
             take 1            skip 1
          subset=[1]         subset=[]
            dfs(1)             dfs(1)
             /   \              /    \
      take 2     skip2    take2      skip2
 subset=[1,2]  subset=[1] subset=[2] subset=[]
    dfs(2)       dfs(2)     dfs(2)     dfs(2)
       |            |           |          |
   save [1,2]   save [1]    save [2]   save []

What each dfs(index) means
dfs(0) → Decide whether to take 1
dfs(1) → Decide whether to take 2
dfs(2) → Decide whether to take 3
dfs(3) → No numbers left → Save the current subset

Notice that every path from the root to a leaf is one subset.

subset.copy() = O(n)

Since there are:

2ⁿ

leaf nodes,

Total time:

O(n × 2ⁿ)

Space Complexity

There are two different answers depending on what the interviewer means.

Auxiliary Space (most interviews)

The recursion stack goes as deep as:

dfs(0)
dfs(1)
dfs(2)
...
dfs(n)

Maximum depth:

n

The subset list also holds at most n elements.

So:

O(n)
"""