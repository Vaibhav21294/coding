"""
Absolutely! Intervals and Greedy Algorithms are two of the most common patterns 
in software engineering interviews. 
They're often taught together because many interval problems are solved using a greedy strategy.

Part 1: Intervals
What is an Interval?

An interval represents a range.

Example:

[2, 5]

means

2 3 4 5

or more generally:

From 2 to 5

Examples in real life:

📅 Meeting from 10:00–11:00
✈️ Flight from 3 PM–7 PM
📺 Movie from 6 PM–9 PM

Representing Intervals in Python
intervals = [
    [1, 3],
    [2, 6],
    [8, 10],
    [15, 18]
]

Each interval has:

[start, end]

Example 1: Merge Intervals
Problem:

[[1,3], [2,6], [8,10], [15,18]]

Notice:

1------3
   2---------6

These overlap.

Merge them:

1-------------6

Final answer:

[[1,6], [8,10], [15,18]]

Step 1: Sort

Always sort by start time.

[[1,3],
 [2,6],
 [8,10],
 [15,18]]

Step 2: Compare

Current interval:

[1,3]

Next interval:

[2,6]

Check:

2 <= 3 ?

Yes.

They overlap.

Merge:

start = min(1,2)=1

end = max(3,6)=6

Result:

[1,6]

Next:

[8,10]

Check

8 <= 6 ?

No.

No overlap.

Add it separately.

Python
"""
def merge(intervals):
    intervals.sort()

    result = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = result[-1][1]

        if start <= last_end:
            result[-1][1] = max(last_end, end)
        else:
            result.append([start, end])

    return result

"""
Output:

print(merge([[1,3],[2,6],[8,10],[15,18]]))
[[1,6],[8,10],[15,18]]

Time:

O(n log n)

because of sorting.

Example 2: Insert Interval

Current intervals:

[[1,2],
 [3,5],
 [6,7],
 [8,10]]

Insert:

[4,8]

After merging:

[[1,2],
 [3,10]]

This is another classic interval interview question.

Example 3: Meeting Rooms

Meetings:

[9,10]

[10,11]

[11,12]

Can one person attend all?

Yes.

Now:

[9,11]

[10,12]

Overlap.

Answer:

No

Part 2: Greedy Algorithms
What is Greedy?

A Greedy Algorithm means:

Always make the best decision right now.

It never looks back.

Real-Life Example

You have:

₹100

Need to pay:

₹87

Greedy approach:

Take the largest note possible.

50

↓

20

↓

10

↓

5

↓

2

Done.

At every step:

Pick the biggest denomination that fits.

Example 1: Minimum Coins

Coins:

1

2

5

10

Need:

18

Greedy:

10

↓

5

↓

2

↓

1

Total:

4 coins

Example 2: Activity Selection

Activities:

A : 1-2

B : 2-3

C : 1-4

D : 3-5

Goal:

Attend the maximum number.

Greedy rule:

Choose the activity that finishes earliest.

Why?

Because it leaves the most time for future activities.

Solution:

A

↓

B

↓

D

Three activities.

If we picked C first:

C

↓

Nothing else

Only one activity.

Python
"""

def activity_selection(intervals):
    intervals.sort(key=lambda x: x[1])

    count = 1
    last_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= last_end:
            count += 1
            last_end = end

    return count

"""
Example 3: Jump Game

Given:

[2,3,1,1,4]

Each number tells you the maximum jump length.

Can you reach the end?

Greedy keeps track of:

Farthest place reachable

If the farthest reachable index always moves forward enough, you can reach the end.

Example 4: Gas Station

Classic interview question.

Gas:

[1,2,3,4]

Cost:

[2,2,2,2]

Where should you start to complete the circle?

A greedy algorithm keeps a running fuel balance and 
resets the starting position whenever the balance becomes negative.

How to Recognize a Greedy Problem

Interview clues:

Maximum number of tasks
Minimum cost
Earliest finish time
Largest profit
Fewest resources
Optimize locally

If the problem asks for a locally optimal choice 
that naturally leads to a global solution, it may be greedy.

Greedy vs Dynamic Programming
| Greedy                          | Dynamic Programming                    |
| ------------------------------- | -------------------------------------- |
| Makes the best immediate choice | Considers many possibilities           |
| Never revisits decisions        | Reuses results of subproblems          |
| Usually faster                  | Often more computation                 |
| Doesn't always work             | Works whenever the recurrence is valid |

Example

Coin denominations:

1, 5, 10, 25

Amount:

30

Greedy:

25

↓

5

Perfect.

Now suppose the coins are:

1, 3, 4

Need:

6

Greedy:

4

↓

1

↓

1

Three coins.

But the optimal answer is:

3

↓

3

Only two coins.

This is why Greedy doesn't always work. 
You must prove (or know) that the greedy choice is always safe for the problem.

Common Interval Interview Problems
Merge Intervals
Insert Interval
Non-overlapping Intervals
Meeting Rooms I & II
Employee Free Time

Common Greedy Interview Problems
Activity Selection
Jump Game
Gas Station
Assign Cookies
Task Scheduler (with variations)
Best Time to Buy and Sell Stock II

Summary
Intervals

Think of intervals whenever you see:

Start and end times
Meeting schedules
Date ranges
Time slots
Overlapping ranges

Typical approach:

Sort the intervals.
Compare adjacent intervals.
Merge or decide based on overlap.

Greedy

Think of greedy whenever you see:

Maximum or minimum objective
Choosing the "best next" option
Scheduling
Resource allocation
Earliest finish or largest immediate gain

Typical pattern:

Identify the locally best choice.
Make that choice.
Never reconsider it.
Continue until the problem is solved.

🎉 Your DSA Interview Roadmap Is Complete

You've now covered the major topics asked in software engineering interviews:

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
✅ Backtracking
✅ Dynamic Programming
✅ Intervals
✅ Greedy Algorithms

These patterns account for the vast majority of coding interview questions 
at companies ranging from startups to large tech firms. 
Once you're comfortable recognizing which pattern a problem belongs to, 
solving the problem becomes much more systematic. 
That's one of the biggest skills interviewers are looking for.
"""