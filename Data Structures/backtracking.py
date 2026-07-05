"""
Absolutely! Backtracking is one of the most important interview techniques. 
It is often confused with Dynamic Programming, but they solve different kinds of problems.

Dynamic Programming: "What is the best answer?"
Backtracking: "Explore every possible choice until you find valid solutions."

A simple way to think about backtracking is:

Try → If it doesn't work, undo it → Try something else.

What is Backtracking?

Backtracking is an algorithmic technique used to solve problems by:

Making a choice.
Exploring where that choice leads.
If it doesn't work, undo the choice.
Try another choice.

It's similar to navigating a maze.

Imagine you're at an intersection:
           Start
          /     \
      Left      Right

You choose Left.

If you hit a dead end:

Start
  |
 Left
  |
Dead End

You return to the intersection and try Right.

That "go back and try again" step is backtracking.

The General Pattern

Almost every backtracking solution follows this structure:

def backtrack(path):
    if solution_found:
        save_answer()
        return

    for choice in choices:
        make_choice(choice)
        backtrack(path)
        undo_choice(choice)

Notice the three important steps:

Choose

↓

Explore

↓

Undo

The undo step is what makes it backtracking.

Example 1: Generate All Subsets

Given:

nums = [1, 2]

Find every subset.

Answer:

[]
[1]
[2]
[1, 2]

Decision Tree

Start with an empty subset.

                 []
              /      \
          Take1     Skip1

If we take 1:

              [1]
             /   \
        Take2   Skip2

If we skip 1:

              []
             /  \
        Take2 Skip2

Complete tree:

                  []
              /         \
            [1]         []
          /    \      /    \
      [1,2]   [1]   [2]    []

Every path from the root to a leaf is one answer.

Python Solution
"""

def subsets(nums):
    result = []

    def backtrack(index, current):
        if index == len(nums):
            result.append(current[:])
            return

        # Choose the current number
        current.append(nums[index])
        backtrack(index + 1, current)

        # Undo the choice
        current.pop()

        # Skip the current number
        backtrack(index + 1, current)

    backtrack(0, [])
    return result

"""
Output:

print(subsets([1, 2]))
[[1, 2], [1], [2], []]

Notice:

current.append(...)

Later:

current.pop()

That's the backtracking step.

Example 2: Permutations

Given:

nums = [1, 2, 3]

Find all permutations.

Answer:

123
132
213
231
312
321

Decision Tree

             []
         /    |    \
        1     2     3

If we choose 1:

        [1]
       /   \
      2     3

Continue until every number has been used.
"""

def permutations(nums):
    result = []

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for num in nums:
            if num in path:
                continue

            path.append(num)
            backtrack(path)
            path.pop()

    backtrack([])
    return result

"""
Again notice:

append()

↓

recursive call

↓

pop()

That is the heart of backtracking.

Example 3: N-Queens

A famous interview problem.

Place queens on a chessboard so that none attack each other.

For a 4×4 board:

. Q . .
. . . Q
Q . . .
. . Q .

Algorithm:

Place a queen.
Check if it's valid.
If valid, continue.
If invalid, remove the queen.
Try another position.

This is classic backtracking.

Example 4: Sudoku Solver

You have a partially filled Sudoku.

Algorithm:

Pick an empty cell.
Try 1.
If valid, continue.
If not, erase it.
Try 2.
Continue until solved.

Again:

Try

↓

Check

↓

Undo

↓

Try again

Visualization

Imagine opening doors.

Door 1

↓

Locked

↓

Go back

↓

Door 2

↓

Locked

↓

Go back

↓

Door 3

↓

Success!

Backtracking is simply systematic trial and error.

Common Interview Problems

Backtracking is commonly used for:

Subsets
Permutations
Combination Sum
N-Queens
Sudoku Solver
Word Search
Palindrome Partitioning
Generate Parentheses

Time Complexity

Backtracking often explores many possibilities, so it can be exponential.

For example:
| Problem      | Complexity  |
| ------------ | ----------- |
| Subsets      | O(2ⁿ)       |
| Permutations | O(n!)       |
| N-Queens     | Exponential |

Backtracking vs DFS

Many people confuse these.

DFS

Goal:

Visit every node in a graph.

Example:

A

↓

B

↓

C

You're exploring an existing structure.

Backtracking

Goal:

Build and explore all possible solutions.

Example:

Choose A

↓

Undo

↓

Choose B

↓

Undo

↓

Choose C

You're constructing solutions as you go.

Relationship: Backtracking is often implemented using recursive DFS, 
but with the added step of undoing choices.

Backtracking vs Dynamic Programming
| Backtracking              | Dynamic Programming                    |
| ------------------------- | -------------------------------------- |
| Explore all possibilities | Reuse previously computed results      |
| Find all valid solutions  | Find the optimal solution or count     |
| Undo choices              | Store answers (memoization/tabulation) |
| Often exponential         | Often polynomial                       |

Examples:

Backtracking

Generate all subsets

Need every answer.

Dynamic Programming

Maximum money you can rob

Need only the best answer.

The Golden Template

If you remember just one thing, remember this template:
"""
def backtrack(path):
    if goal_reached:
        save(path)
        return

    for choice in choices:
        make_choice(choice)

        backtrack(path)

        undo_choice(choice)
"""        

Think of it as:

Choose

↓

Explore

↓

Undo

↓

Choose next

When Should You Think "Backtracking"?

Interview clues include:

Generate all combinations.
Generate all permutations.
Find every valid arrangement.
Explore every possible path.
Solve puzzles like Sudoku or N-Queens.

If the problem asks for all possible solutions, backtracking is often the right approach.

Your Interview Learning Journey

You've now covered the major DSA topics used in software engineering interviews:

✅ Arrays & Strings
✅ Hash Maps
✅ Linked Lists
✅ Stacks & Queues
✅ Trees & Binary Trees
✅ Binary Search Trees
✅ Graphs (BFS & DFS)
✅ Heaps / Priority Queues
✅ Two Pointers
✅ Sliding Window
✅ Binary Search
✅ Recursion
✅ Dynamic Programming
✅ Backtracking
What I'd recommend next

Now that you've learned the core concepts, the next step is pattern-based practice. 
Rather than solving random problems, practice by pattern:

Two Pointers – 5 problems
Sliding Window – 5 problems
Binary Search – 5 problems
Trees (DFS/BFS) – 8–10 problems
Graphs – 8–10 problems
Heap – 5 problems
Backtracking – 5 problems
Dynamic Programming – 8–10 problems

This approach helps you recognize patterns quickly during interviews, 
which is much more effective than memorizing individual solutions.
"""