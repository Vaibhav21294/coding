"""
Binary Search
What problem does it solve?

Binary Search helps you find an element in a sorted array efficiently.

Instead of checking every element one by one, 
Binary Search repeatedly eliminates half of the remaining search space.

Example

Given:

nums = [2, 5, 8, 12, 16, 23, 38, 56, 72]
target = 23

We want to find:

23

Brute Force Approach

Check every element.

for i in range(len(nums)):
    if nums[i] == target:
        return i
Time Complexity

One loop:

O(N)
Space Complexity

No extra data structures:

O(1)

Binary Search Idea

Instead of checking every element:

Look at the middle element.
If it's the target → Done.
If the target is smaller → Search the left half.
If the target is larger → Search the right half.

Each comparison removes half of the remaining elements.
"""

class Solution:
    def search(self, nums, target):

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
Time Complexity

Each iteration cuts the search space in half.

O(log N)

No extra arrays.

O(1)

When can Binary Search be used?

This is one of the most common interview questions.

You should immediately think of Binary Search when:

✅ The data is sorted.
✅ You need to find a value.
✅ You need the first or last occurrence of a value.
✅ You're looking for a point where a condition changes 
(for example, the first True in a sequence of False, False, True, True).

Common LeetCode Problems
Binary Search (Easy)
Search Insert Position (Easy)
First Bad Version (Easy)
Search in Rotated Sorted Array (Medium)
Find First and Last Position of Element in Sorted Array (Medium)
Find Minimum in Rotated Sorted Array (Medium)
Koko Eating Bananas (Medium) (Binary Search on the answer)

Interview Explanation (30 seconds)

"Since the array is sorted, I can use Binary Search instead of Linear Search. 
I compare the target with the middle element. 
If the target is smaller, I search the left half; otherwise, I search the right half. 
Each iteration halves the remaining search space, resulting in a time complexity of O(log N) and a space complexity of O(1)."

Interview Tip

A good mental checklist is:

Is the array sorted?
Can I eliminate half of the remaining search space after each comparison?

If the answer to both is yes, Binary Search is often the right approach.
"""