"""
Excellent! Number of Islands is one of the most frequently asked Graph (DFS/BFS) interview questions.

It looks like a matrix problem, but interviewers expect you to recognize it as a graph traversal problem.

Problem Statement

You are given a grid of '1's (land) and '0's (water).

Return the number of islands.

An island is formed by connecting adjacent land cells horizontally or vertically (not diagonally).

Example:

grid =

[
 ["1","1","0","0","0"],
 ["1","1","0","0","0"],
 ["0","0","1","0","0"],
 ["0","0","0","1","1"]
]

Answer:

3

There are:

Island 1

1 1
1 1
Island 2

1
Island 3

1 1

Why is this a Graph problem?

Imagine each land cell ('1') is a node.

If two land cells touch horizontally or vertically, there's an edge between them.

Example:

1 1
1 1

can be visualized as:

A --- B
|     |
C --- D

All four nodes are connected, so they form one island.

The problem becomes:

How many connected components are in the graph?

Intuition

Suppose the grid is:

1 1 0
1 0 0
0 0 1

Start scanning from the top-left.

You find:

1

This must be a new island.

Count:

islands = 1

Now explore every connected land cell from here using DFS (or BFS).

Mark them as visited.

Continue scanning.

When you later reach the bottom-right 1, it's unvisited, so it's a new island.

Count becomes:

2

Algorithm

For every cell:

* If it's water ('0'), ignore it.
* If it's already visited, ignore it.
* If it's unvisited land ('1'):
    *Increment the island count.
    * Run DFS to visit the entire island.

DFS Solution (Most Common)
"""

class Solution:

    def numIslands(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        def dfs(r, c):

            # Out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Water
            if grid[r][c] == "0":
                return

            # Already visited
            if grid[r][c] == "#":
                return

            # Mark visited
            grid[r][c] = "#"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands

"""
Dry Run

Grid:

1 1 0
1 0 0
0 0 1

Initially:

Islands = 0
Scan (0,0)

It's land.

Increment:

Islands = 1

Run DFS.

DFS visits:

1 1
1

Marks them:

# # 0
# 0 0
0 0 1

Continue scanning.

Everything in the first island is already visited.

Skip them.

Reach:

(2,2)

It's land.

Increment:

Islands = 2

Run DFS.

Grid becomes:

# # 0
# 0 0
0 0 #

Done.

Answer:

2

Why do we mark visited?

Suppose we don't.

1 1
1 1

Starting at the top-left:

You visit the top-right.

The top-right visits the top-left again.

The top-left visits the top-right again.

This repeats forever.

Marking a cell as visited prevents revisiting it.

In this solution, we reuse the grid by changing "1" to "#".

You could also keep a separate visited set, but modifying the grid saves space.

Why 4 DFS Calls?

From every land cell, you can move in four directions:

      Up
       ↑
Left ← X → Right
       ↓
     Down

That's why we call:

dfs(r+1, c)   # Down
dfs(r-1, c)   # Up
dfs(r, c+1)   # Right
dfs(r, c-1)   # Left

Time Complexity

Let:

R = number of rows
C = number of columns

Total cells:

R × C

Each cell is visited at most once.

Therefore:

Time = O(R × C)

Space Complexity

The recursion stack can grow as large as the size of one island.

Worst case:

1 1 1
1 1 1
1 1 1

The entire grid is one island.

DFS may recurse through all cells.

So:

Space = O(R × C)

If the grid is sparse or balanced, the recursion depth is often much smaller, 
but the worst-case bound is still O(R × C).

Complexity Summary
| Complexity | Value                                     |
| ---------- | ----------------------------------------- |
| **Time**   | **O(R × C)**                              |
| **Space**  | **O(R × C)** (worst-case recursion stack) |

How to recognize this problem

Whenever you see:

A 2D grid
Connected cells
Count groups / islands / regions
Horizontal & vertical movement

Think:

"This is a graph traversal problem (DFS or BFS)."

Interview Thought Process

A good explanation is:

"I'll scan every cell in the grid. Whenever I find an unvisited land cell ('1'), I've discovered a new island, so I increment my count. Then I use DFS to visit and mark every land cell connected to it. This ensures each island is counted exactly once. Since every cell is visited at most once, the time complexity is O(R × C)."

A pattern you'll reuse

This exact DFS/BFS pattern appears in many interview questions, such as:

Number of Islands
Max Area of Island
Flood Fill
Surrounded Regions
Rotting Oranges (using BFS)
Pacific Atlantic Water Flow

Once you're comfortable with this traversal pattern, many grid-based graph problems become much easier.

Absolutely! A smaller grid is much easier to understand.

Let's use this 3 × 2 grid (3 rows, 2 columns):

[
 ["1", "1"],
 ["0", "1"],
 ["1", "0"]
]

Coordinates:

      c0 c1

r0     1  1
r1     0  1
r2     1  0

There are 2 islands here:

Island 1:

1 1
  1

Island 2:

1
Initial State
islands = 0

Grid:

      c0 c1

r0     1  1
r1     0  1
r2     1  0
Step 1: Start scanning

The outer loops start at:

(r0, c0)

Cell value:

1

It's land!

So:

islands = 1

Now call:

dfs(0, 0)
DFS at (0,0)

Current position:

 X 1
 0 1
 1 0

Mark it visited:

 # 1
 0 1
 1 0

Now DFS explores 4 directions.

Down

Go to:

(1,0)

Grid:

 # 1
 X 1
 1 0

Value:

0

Water.

Return immediately.

Up

Go to:

(-1,0)

Outside the grid.

Return.

Right

Go to:

(0,1)

Grid:

 # X
 0 1
 1 0

Land!

Mark visited.

 # #
 0 1
 1 0

Now DFS continues from (0,1).

Down

Go to:

(1,1)

Grid:

 # #
 0 X
 1 0

Land!

Mark visited.

 # #
 0 #
 1 0

Explore its neighbors:

Down → (2,1) = 0 ❌
Up → (0,1) = # ❌
Left → (1,0) = 0 ❌
Right → Outside ❌

Nothing more to visit.

Return.

Back to (0,1)

Continue remaining directions:

Up → Outside ❌
Right → Outside ❌
Left → Already visited (#) ❌

Return.

Back to (0,0)

Continue remaining direction:

Left:

Outside.

Return.

DFS is complete.

Grid after first DFS
 # #
 0 #
 1 0

Notice:

The entire first island has been marked.

Continue scanning

Outer loops continue.

(0,1)

Already visited (#).

Skip.

(1,0)

Water.

Skip.

(1,1)

Visited.

Skip.

(2,0)

Cell value:

1

Aha!

This is an unvisited land cell.

So:

islands = 2

Call:

dfs(2,0)
DFS at (2,0)

Current grid:

 # #
 0 #
 X 0

Mark visited.

 # #
 0 #
 # 0

Check neighbors:

Down → Outside ❌
Up → Water ❌
Left → Outside ❌
Right → Water ❌

Done.

Continue scanning

Last cell:

(2,1)

Water.

Skip.

Outer loops finish.

Final Answer
islands = 2
What are the outer loops doing?

The outer loops simply ask:

"Have I found a NEW island?"

They scan every cell:

(0,0) ✔ New island

(0,1) Already visited

(1,0) Water

(1,1) Already visited

(2,0) ✔ New island

(2,1) Water
What is DFS doing?

DFS's only job is:

"Starting from one land cell, visit every land cell connected to it."

So when we start at (0,0), DFS automatically visits:

(0,0)
(0,1)
(1,1)

They all belong to the same island.

Later, when the outer loops reach (0,1) or (1,1), they're already marked as visited, so we don't count them again.

The two-part algorithm to remember
Outer loops:
    Find a new island.

DFS:
    Mark the entire island as visited.

Repeat until every cell has been scanned.

This separation of responsibilities is the key idea behind Number of Islands. 
Once you see it this way, the algorithm becomes much easier to reason about.

"""