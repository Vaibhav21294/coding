"""
Problem Statement

Given a string s, find the length of the longest substring without repeating characters.

A substring means the characters must be contiguous.

Example 1
Input:
s = "abcabcbb"

Output:
3

Explanation:

The longest substring is:

"abc"

Length:

3

Example 2
Input:
s = "bbbbb"

Output:
1

The longest substring is:

"b"

Example 3
Input:
s = "pwwkew"

Output:
3

The answer is:

"wke"

Length:

3

Brute force
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length = 0

        for i in range(len(s)):

            for j in range(i, len(s)):

                substring = s[i:j+1]

                if len(substring) == len(set(substring)):
                    max_length = max(max_length, len(substring))
                else:
                    break

        return max_length

"""
Final Complexity
Complexity	Value
Time	O(N³)
Space	O(N)

Yes! That's actually a perfectly reasonable way to explain it in an interview.

You can say:

"There are two nested loops, which generate O(N²) substrings. 
For each substring, we create the substring and traverse it to build a set, which takes O(N) in the worst case. 
Therefore, the total time complexity is O(N² × N) = O(N³)."

"At any point in time, the largest substring we create can have length N, so it requires O(N) space."

Optimized Idea (Sliding Window)

Instead of restarting from every index, maintain a window of unique characters.

Use:

left → start of the window
right → end of the window

The window always contains unique characters.

If a duplicate appears:

Move left forward until the duplicate is removed.

Algorithm

Use:

left
right
set

For every character:

If it's already in the set:

Remove characters from the left.
Move left.

Then:

Add current character.
Update maximum length.
"""

def lengthOfLongestSubstring(s):

    seen = set()

    left = 0
    max_length = 0

    for right in range(len(s)):

        while s[right] in seen:

            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        max_length = max(max_length, right - left + 1)

    return max_length

"""
Why is this O(N)?

At first glance, there's a for loop and a while loop, so it looks like O(N²).

The key insight is:

right moves from left to right exactly N times.
left also moves from left to right exactly N times.

Neither pointer ever moves backward.

So each character is:

Added to the set at most once.
Removed from the set at most once.

Total work:

O(N)

Time Complexity
O(N)

Space Complexity

The set stores at most one copy of each character in the current window.

Worst case (all characters are unique):

O(N)

"""