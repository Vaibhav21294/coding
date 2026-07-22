"""
Problem Statement

You are given a sorted array that has been rotated at an unknown pivot.

Example:

nums = [4,5,6,7,0,1,2]
target = 0

Return the index of target.

Answer:

4

What is a Rotated Sorted Array?

Originally:

0 1 2 4 5 6 7

After rotation:

4 5 6 7 0 1 2

Another example:

6 7 8 1 2 3 4 5

Notice:

It is not completely sorted.
But one half is always sorted.

That observation is the key to solving this problem.

Brute Force
for i in range(len(nums)):
    if nums[i] == target:
        return i
Complexity

Time:

O(N)

Space:

O(1)

Why can't we use normal Binary Search?

Consider:

4 5 6 7 0 1 2

Target:

0

Normal Binary Search:

left = 0
right = 6

mid = 3

nums[mid] = 7

Since:

0 < 7

A normal Binary Search would search the left half.

But that's wrong!

The target is actually in the right half.

So we need another idea.

The Key Observation

At every step:

One of the two halves is guaranteed to be sorted.

Example:

4 5 6 | 7 | 0 1 2
        ↑
       mid

Left half:

4 5 6 7

Sorted ✅

Right half:

0 1 2

Not relevant here.

Another example:

6 7 | 1 | 2 3 4
      ↑

Right half:

1 2 3 4

Sorted ✅

Python Code
"""

class Solution:
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:

                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:

                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
    
"""
Why does this work?

At every step:

One half is sorted.
If the target lies inside that sorted half, search it.
Otherwise, search the other half.

Just like Binary Search, we eliminate half of the array every iteration.

Time Complexity

Each iteration removes half the search space.

O(log N)
Space Complexity

Only:

left
right
mid

No extra arrays.

O(1)
Complexity Summary
Approach	Time	Space
Brute Force	O(N)	O(1)
Binary Search	O(log N)	O(1)
How to recognize this problem in interviews

Whenever you see:

A sorted array
But it has been rotated
And you need to search for a value

Think:

"This is Binary Search with an extra check to determine which half is sorted."

Interview Tip

A good way to remember the core logic is to ask these questions in every iteration:

Did I find the target?
Which half is sorted?
Is the target inside the sorted half?
If yes, search that half; otherwise, search the other half.

If you can answer those four questions, you can derive the solution even if you don't remember the exact code.

I dont understand the algo..you are saying one half is always sorted

but in this case nums=[4,5,6,7,0,1,2]

4 to 7 are sorted..also 0 to 2 are sorted

Excellent question! This is exactly where most people get stuck.

You're absolutely right:

For

[4,5,6,7,0,1,2]

both of these are sorted:

4 5 6 7   ✅

0 1 2     ✅

So why do people say "one half is always sorted"?

The statement is actually incomplete.

A more accurate statement is:

After choosing left, mid, and right, at least one of the two halves (left...mid or mid...right) is guaranteed to be sorted.

It's not talking about the original array—it refers to the current search window during Binary Search.

Let's see why.

Initially
Index: 0 1 2 3 4 5 6

Value: 4 5 6 7 0 1 2

Initially:

left = 0
right = 6

mid = 3

So we split the current search window into:

Left Half
4 5 6 7

Right Half
0 1 2

Yes!

Both happen to be sorted in this first iteration.

That's perfectly okay.

The algorithm only needs at least one sorted half.

Another example

Suppose after one iteration we search only:

4 5 6 7

Now

left = 0
right = 3

mid = 1

Split:

4 5

6 7

Again:

Both are sorted.

Still okay.

Now look at another rotated array
6 7 8 1 2 3 4 5

Initially

left = 0

right = 7

mid = 3

Split:

6 7 8 1

2 3 4 5

Left:

6 7 8 1

Not sorted ❌

Right:

2 3 4 5

Sorted ✅

Here only one half is sorted.

Another example
5 6 7 1 2 3 4

Split:

5 6 7 1

2 3 4

Left:

Not sorted.

Right:

Sorted.

Why do we check this?

The important question isn't:

"Are both halves sorted?"

The important question is:

Which half can I trust?

If one half is sorted, then we can easily determine whether the target belongs there.

Example
4 5 6 7 | 0 1 2

Target:

1

We know:

4 5 6 7

is sorted.

Can 1 exist there?

We simply check:

4 <= 1 < 7

No.

Therefore we know with certainty:

Ignore left half.

Search the right half.

Why does this condition work?
if nums[left] <= nums[mid]:

For our example:

nums[left] = 4

nums[mid] = 7

Is

4 <= 7

Yes.

That tells us:

The left half is sorted.

Now consider

6 7 8 1 2 3 4 5

Initially

left = 0

mid = 3

Values:

nums[left] = 6

nums[mid] = 1

Is

6 <= 1

No.

Therefore:

The left half cannot be sorted.

So the right half must be sorted.

A better way to remember

Don't remember:

"One half is always sorted."

Remember:

"Every Binary Search iteration asks: Which side is sorted?"

Then:

Identify the sorted half.
Check if the target belongs there.
If yes, search it.
Otherwise, search the other half.
One important insight

You noticed that in the first example both halves are sorted. That's absolutely correct.

The algorithm still works because it only checks the left half first:

if nums[left] <= nums[mid]:

If that's true, it uses the left half to make the decision. It doesn't matter that the right half also happens to be sorted in that iteration.

I think what would help you most is a visual animation-style dry run where we move left, mid, and right step by step and color which half is sorted in each iteration. That usually makes this problem "click" in about 5 minutes.

then we are doing binary search on this problem too right? what is the difference?

YES! 🎯 That's the key insight.

This problem is Binary Search.

The only difference is that before deciding which half to search, we first identify which half is sorted.

Let's compare the two side by side.

Normal Binary Search

Array:

2 5 8 12 16 23 38 56

Suppose the target is:

23

We calculate:

mid = (left + right) // 2

Now compare:

if target < nums[mid]:

Go left.

Otherwise:

Go right.

That's it.

Because the ENTIRE array is sorted.

Rotated Sorted Array

Now consider:

4 5 6 7 0 1 2

Suppose

target = 0

Again we calculate

mid = (left + right) // 2

We get

4 5 6 [7] 0 1 2

Now imagine we use normal Binary Search.

We ask:

target < nums[mid]
0 < 7

Yes.

So Binary Search would go LEFT.

But the answer is actually on the RIGHT!

That's why normal Binary Search fails.

So what extra step do we add?

Instead of immediately deciding:

Go left or right

we first ask:

Which half is sorted?

For this array:

4 5 6 7 | 0 1 2

The left half

4 5 6 7

is sorted.

Now we ask another question:

Can my target possibly exist inside this sorted half?

The target is

0

Is

4 <= 0 < 7

No.

Therefore:

It cannot be in the left half.

So we search the right half.

Compare both algorithms
Normal Binary Search
mid = (left + right)//2

if nums[mid] == target:
    return mid

elif target < nums[mid]:
    right = mid - 1

else:
    left = mid + 1

Only one comparison decides the direction.

Rotated Binary Search
mid = (left + right)//2

if nums[mid] == target:
    return mid

# Figure out which half is sorted

if nums[left] <= nums[mid]:

    # Left is sorted

    if nums[left] <= target < nums[mid]:
        right = mid - 1
    else:
        left = mid + 1

else:

    # Right is sorted

    if nums[mid] < target <= nums[right]:
        left = mid + 1
    else:
        right = mid - 1

Notice that the pointer updates are exactly the same:

left = mid + 1

right = mid - 1

The only extra logic is deciding which half we should trust.

Think of it this way
Normal Binary Search

You know the entire array is sorted.

So one comparison is enough.

Target < mid?

Yes → Left

No → Right
Rotated Binary Search

The entire array is not sorted.

Only one half is sorted.

So first you ask:

Which half is sorted?

Then:

Does the target belong there?

Then move left or right.

This is how I remember it
Normal Binary Search

        mid
         ↓
2 5 8 12 16 23 38

↓

Target < mid ?

↓

Go Left / Right
Rotated Binary Search

        mid
         ↓
4 5 6 7 0 1 2

↓

Which half is sorted?

↓

Can target be inside that half?

↓

Go Left / Right
The biggest takeaway

Rotated Sorted Array is not a new algorithm.

It is simply:

Binary Search + one extra check to determine which half is sorted before eliminating half of the search space.

That's why its time complexity is still O(log N)—you're still discarding half of the search space in every iteration, 
just with a smarter decision about which half to discard.

Time Complexity

Each iteration removes half the search space.

O(log N)
Space Complexity

Only:

left
right
mid

No extra arrays.

O(1)

Complexity Summary
| Approach      | Time         | Space    |
| ------------- | ------------ | -------- |
| Brute Force   | O(N)         | O(1)     |
| Binary Search | **O(log N)** | **O(1)** |

How to recognize this problem in interviews

Whenever you see:

A sorted array
But it has been rotated
And you need to search for a value

Think:

"This is Binary Search with an extra check to determine which half is sorted."

Interview Tip

A good way to remember the core logic is to ask these questions in every iteration:

Did I find the target?
Which half is sorted?
Is the target inside the sorted half?
If yes, search that half; otherwise, search the other half.

If you can answer those four questions, you can derive the solution even if you don't remember the exact code.

"""