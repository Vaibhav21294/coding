"""
Binary Search is one of the highest-value algorithms for software engineering interviews. 
It's tested directly and also appears in many "search on answer" problems.

What is Binary Search?

Instead of checking every element one by one, Binary Search repeatedly cuts the search space in half.

This is only possible when the data is sorted.

Imagine looking up a word in a dictionary. 
You don't start at page 1—you open roughly in the middle, 
then decide whether to go left or right. That's Binary Search.

Example
Suppose we have:
nums = [2, 5, 8, 12, 16, 23, 38, 56, 72]
Find:
23

Linear Search
Check every element:
2
5
8
12
16
23 ✓

Worst case:
O(n)

Binary Search
Start:
Index

0 1 2 3 4 5 6 7 8

Value

2 5 8 12 16 23 38 56 72

We keep track of three variables:
left = 0
right = 8

Step 1
Find the middle.
mid = (left + right) // 2

mid = (0 + 8) // 2 = 4

Middle value:
16

Visualization:
2 5 8 12 16 23 38 56 72
L       M             R

Is
16 == 23 ?
No.

Is
16 < 23 ?
Yes.

So the answer must be to the right.

Update:
left = mid + 1

Now:
2 5 8 12 16 23 38 56 72
          L  M      R

Step 2
Now
left = 5
right = 8

Compute middle.
mid = (5 + 8) // 2
mid = 6

Middle value:
38

Visualization:
23 38 56 72
L  M      R

Compare:
38 > 23

Search left half.
right = mid - 1

Now:
23 38
L R

Step 3
Now
left = 5
right = 5

Middle:
23
Found!

Python Code
"""

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1

"""
Example:
nums = [2, 5, 8, 12, 16, 23, 38, 56, 72]

print(binary_search(nums, 23))

Output:
5

because
nums[5] = 23

Why is it so fast?
Suppose you have 1,000,000 numbers.

Linear Search
Worst case:
1,000,000 comparisons

Binary Search
Each step cuts the search space in half:
1,000,000

↓

500,000

↓

250,000

↓

125,000

↓

...
After only about 20 comparisons, you've narrowed it down to one element!

Time Complexity
| Algorithm     | Time     |
| ------------- | -------- |
| Linear Search | O(n)     |
| Binary Search | O(log n) |

This is why Binary Search is one of the fastest search algorithms for sorted data.

When should you think of Binary Search?
Common clues include:

The array is sorted.
The question asks you to find an element efficiently.
You're looking for the first or last occurrence of a value.
The problem asks for the minimum or maximum value that 
satisfies a condition (often called binary search on the answer).

Interview Example: First Occurrence
Given:
nums = [1, 2, 2, 2, 3, 4]
Find the first occurrence of 2.
A regular Binary Search may return index 1, 2, or 3, depending on which 2 it lands on.

To find the first occurrence:

If you find 2, save the index.
Continue searching the left half for an earlier occurrence.
When the search finishes, return the saved index.

This small modification is a common interview variation.

Key Takeaways
Prerequisite: The data must usually be sorted.
Keep three variables: left, right, and mid.
At each step:
If nums[mid] == target: return it.
If nums[mid] < target: search the right half.
Otherwise: search the left half.
Each iteration halves the remaining search space, giving a time complexity of O(log n).

For interview preparation, I recommend learning Binary Search in this order:

Standard Binary Search
First/Last Occurrence
Search Insert Position
Search in Rotated Sorted Array
Binary Search on the Answer (e.g., minimum speed, capacity, or time problems)

These five patterns cover the vast majority of Binary Search questions 
you'll encounter in software engineering interviews.
"""