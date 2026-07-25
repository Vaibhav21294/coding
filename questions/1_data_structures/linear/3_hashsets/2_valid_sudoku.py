"""
Problem

Determine if a partially filled 9×9 Sudoku board is valid.

A valid Sudoku must satisfy:

Each row contains digits 1-9 without duplicates.
Each column contains digits 1-9 without duplicates.
Each 3×3 box contains digits 1-9 without duplicates.

Ignore "." cells.

Example:
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9

2. Better Solution (Hash Sets)

Instead of comparing every pair of cells, use a set.

Check each row

Example:

5 3 . . 7 . . . .

Create an empty set.

{}

Read numbers one by one.

5 -> add

{5}

3 -> add

{5,3}

7 -> add

{5,3,7}

If you ever see

5

again:

Already in set

Return False
Check each column

Do the exact same thing.

Instead of fixing the row, fix the column.

Check each 3×3 box

For the first box:

5 3 .
6 . .
. 9 8

Again:

{}

Add numbers.

If any number already exists, return False.

Code (Three Separate Checks)
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Rows
        for row in range(9):
            seen = set()

            for col in range(9):
                value = board[row][col]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # Columns
        for col in range(9):
            seen = set()

            for row in range(9):
                value = board[row][col]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # 3x3 Boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):

                seen = set()

                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):

                        value = board[r][c]

                        if value == ".":
                            continue

                        if value in seen:
                            return False

                        seen.add(value)

        return True
    
"""
Complexity

Generalized to an N × N board:

Time: O(N²)
Space: O(N)

For the actual 9×9 Sudoku:

Time: O(1)
Space: O(1)

because the board size never changes.

3. Optimal Solution (One Pass)

There is a clever solution that uses three dictionaries of sets:

rows = {}
cols = {}
boxes = {}

Then you traverse the board once.

For every digit:

Check its row set.
Check its column set.
Check its box set.

This avoids three separate passes.

However, I don't recommend learning this one first.

A useful rule for nested loops

Don't count the number of loops.

Count the total number of iterations.

For example:

for i in range(n):
    for j in range(n):

Total:

n × n = n²

Now consider:

for i in range(n):
    for j in range(3):

Total:

n × 3 = 3n

Big-O:

O(n)

Even though there are two loops.

Similarly, in Sudoku:

for box_row in range(0, 9, 3):

is not an n loop.

It runs only √N times in the generalized case (or just 3 times for a standard Sudoku).
"""