"""
This is one of the most frequently asked medium-level interview questions. 
It teaches the Prefix/Suffix Array pattern.

Problem Statement

Given an integer array nums, return an array answer such that:

answer[i] = product of all elements in nums except nums[i]

Constraints:

Do not use division.
The solution should run in O(n) time.

Example 1
Input:
nums = [1, 2, 3, 4]

Output:
[24, 12, 8, 6]

Explanation:

answer[0] = 2 × 3 × 4 = 24

answer[1] = 1 × 3 × 4 = 12

answer[2] = 1 × 2 × 4 = 8

answer[3] = 1 × 2 × 3 = 6

Example 2
Input:
nums = [-1, 1, 0, -3, 3]

Output:
[0, 0, 9, 0, 0]

Brute Force Solution

For every index, multiply all the other elements.
"""

def product_except_self(nums):
    answer = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product = product * nums[j]
        answer.append(product)
    return answer

"""
Time Complexity

Two nested loops.

O(n²)
Space Complexity

Ignoring the output array:

O(1)

(Output array itself is required.)

Optimized Idea

Suppose

nums = [1,2,3,4]

For index 2 (value = 3)

We need

1 × 2 × 4

Notice:

(product on the LEFT)
×

(product on the RIGHT)

Instead of recomputing these every time, let's precompute them.

Prefix Products

Prefix means:

Product of everything before the current index.

For

[1,2,3,4]

Prefix array becomes

[1,1,2,6]

Why?

Index	Prefix Product
0	1
1	1
2	1×2 = 2
3	1×2×3 = 6

Suffix Products

Suffix means:

Product of everything after the current index.

[1,2,3,4]

Suffix array becomes

[24,12,4,1]
Index	Suffix Product
0	2×3×4 = 24
1	3×4 = 12
2	4
3	1

Now:

Answer[i] = Prefix[i] × Suffix[i]

Example:

Index = 2

Prefix = 2

Suffix = 4

Answer = 8

Exactly correct.

Python Solution (Prefix + Suffix Arrays)
"""

def product_except_self(nums):
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    answer = [1] * n

    for i in range(1, n):
        prefix[i] = prefix[i-1] * nums[i-1]

    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]
    
    for i in range(n):
        answer[i] = prefix[i] * suffix[i]
    
    return answer

"""
Dry Run

Input

nums = [1,2,3,4]
Step 1

Build Prefix

prefix

[1,1,2,6]
Step 2

Build Suffix

suffix

[24,12,4,1]

Step 3

Multiply
| Prefix | Suffix | Answer |
| ------ | ------ | ------ |
| 1      | 24     | 24     |
| 1      | 12     | 12     |
| 2      | 4      | 8      |
| 6      | 1      | 6      |

Final answer

[24,12,8,6]

Time Complexity

Three passes.

O(n)
Space Complexity

Three extra arrays.

O(n)

Even Better Solution (Interview Favorite)

The interviewer will often ask:

"Can you do it using only the output array?"

The answer is Yes.

Instead of keeping separate prefix and suffix arrays:

Store prefix products directly in the output array.
Use one variable to track the suffix product while traversing backwards.

Optimized Python Solution
"""

def product_except_self(nums):

    n = len(nums)
    answer = [1] * n

    # Prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer

"""
Dry Run of Optimized Solution

Input:

nums = [1,2,3,4]
First Pass (Prefix)
Index	Answer	Prefix
0	1	1
1	1	2
2	2	6
3	6	24

Answer becomes

[1,1,2,6]

Second Pass (Suffix)

Start:

suffix = 1
Index	Answer Before	Suffix	Answer After
3	6	1	6
2	2	4	8
1	1	12	12
0	1	24	24

Final

[24,12,8,6]

Complexity of Optimized Solution
Metric	Complexity
Time	O(n)
Extra Space	O(1) (excluding the required output array)

This is the solution interviewers are typically looking for.

Interview Explanation (30 seconds)

If the interviewer asks, "How did you optimize it?", you can say:

"The brute-force approach recalculates the product for every index, resulting in O(n²) time. 
Instead, I compute the product of all elements to the left and all elements to the right of each index. 
I first store the prefix products in the output array, 
then traverse from right to left while maintaining a running suffix product and multiply it into the output. 
This gives an O(n) solution with O(1) extra space, excluding the output array."

💡 Pattern to Remember

This problem teaches the Prefix/Suffix pattern.

Whenever a problem asks:

"For every index, compute something using all elements before and after it."

Think:

Prefix (left-to-right)
Suffix (right-to-left)

This same pattern appears in several other interview problems, making it an important one to recognize.
"""


