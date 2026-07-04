"""
2. Sliding Window

Sliding Window is actually a special application of two pointers.

Instead of comparing two ends, the two pointers define a window over a contiguous part of the array or string.

Example
Array

1 2 3 4 5 6

Window

[2 3 4]

Then the window slides:
1 [2 3 4] 5 6

↓

1 2 [3 4 5] 6

↓

1 2 3 [4 5 6]

Example 1: Maximum Sum of Size K
Problem:
nums = [2,1,5,1,3,2]

k = 3

Find maximum sum of any 3 consecutive numbers.

Possible sums:
2+1+5 = 8

1+5+1 = 7

5+1+3 = 9

1+3+2 = 6

Answer:
9

Brute Force
max_sum = 0

for i in range(len(nums)-k+1):
    current = sum(nums[i:i+k])
    max_sum = max(max_sum,current)

Time:
O(n*k)

Sliding Window
First window
2 1 5

sum = 8

Slide one step
Remove
2

Add
1

New sum
8 - 2 + 1 = 7

Slide
Remove
1

Add
3

7 -1 +3 =9

No need to recompute the whole sum.
"""

from sqlite3 import Time


def max_sum(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i - k]

        max_sum = max(max_sum, window_sum)

    return max_sum

"""
Output
print(max_sum([2,1,5,1,3,2],3))

9

Time
O(n)

Example 2: Longest Substring Without Repeating Characters
Given:
s = "abcabcbb"

Answer:
"abc"

Length = 3

Window:
abc

↓

abca

Oops!

'a' repeated.

Move left pointer.

↓

bca
"""

def length_of_longest_substring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

"""
Time
O(n)

When should you think of Two Pointers vs. Sliding Window?
| Clue in the problem                   | Technique      |
| ------------------------------------- | -------------- |
| Sorted array and looking for a pair   | Two Pointers   |
| Reverse an array/string in place      | Two Pointers   |
| Palindrome checking                   | Two Pointers   |
| Merge two sorted arrays               | Two Pointers   |
| Consecutive/contiguous subarray       | Sliding Window |
| Longest/shortest substring            | Sliding Window |
| Fixed-size window (e.g., size `k`)    | Sliding Window |
| Variable-size window with constraints | Sliding Window |

Interview Tip

When you see words like:

pair
sorted array
left/right
palindrome
reverse

think Two Pointers.

When you see:

contiguous
subarray
substring
window
longest
smallest
maximum sum of k elements

think Sliding Window.

Mastering these patterns can turn many problems that look like O(n²) 
into elegant O(n) solutions, 
which is exactly what interviewers often look for.
"""




