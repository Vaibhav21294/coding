"""
Two Sum II - Input Array Is Sorted is one of the most important Two Pointers problems.

Problem

You're given:

A sorted array.
A target.

Return the 1-indexed positions of the two numbers whose sum equals the target.

Example:

numbers = [2,7,11,15]
target = 9

Output:
[1,2]

Because

2 + 7 = 9

Solution 3: Optimal (Two Pointers)
Why does it work?

Suppose

numbers = [2,7,11,15]
target = 9

Start:

L              R

2   7   11   15

Current sum

2 + 15 = 17

Too large.

Since the array is sorted,

moving the right pointer left decreases the sum.

Move right.
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:

            current = numbers[left] + numbers[right]

            if current == target:
                return [left + 1, right + 1]

            elif current < target:
                left += 1

            else:
                right -= 1

"""
Complexity

Time:

O(n)

Each pointer moves at most n times.

Space:

O(1)

Pattern Recognition

Whenever you see:

Sorted array
Need to find a pair
Sum, difference, or comparison between two values

your first thought should be:

Can I solve this with two pointers instead of a hash map?

That's one of the most common interview patterns, 
and interviewers often include the word "sorted" specifically to see if you recognize it.
"""