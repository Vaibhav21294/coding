"""
Absolutely! Dynamic Programming (DP) is often considered the hardest topic in coding interviews. 
The good news is that once you understand the core idea, many DP problems follow similar patterns.

The biggest misconception is that DP is a completely new algorithm. 
It's actually an optimization technique for recursive problems.

What is Dynamic Programming?

Dynamic Programming is used when:

The same problem is solved over and over (overlapping subproblems).
We can save those answers and reuse them instead of recomputing them.

Think of it as:

Don't solve the same problem twice.

A Real-Life Analogy

Imagine climbing a staircase.

There are 100 steps.

Every time you reach step 50, you calculate:

"How many ways can I reach the top from here?"

If you calculate that answer every time you reach step 50, you're wasting work.

Instead:

Step 50

↓

Answer = 89 ways

↓

Save it

↓

Next time reuse it

That's Dynamic Programming.

Example 1: Fibonacci Numbers

This is the classic DP example.

The Fibonacci sequence is:

0, 1, 1, 2, 3, 5, 8, 13, 21...

Formula:

F(n) = F(n-1) + F(n-2)

Recursive Solution
def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

Find:

fib(5)

Looks simple.

But here's what actually happens.

Call Tree
                 fib(5)
               /        \
          fib(4)       fib(3)
         /     \       /     \
    fib(3) fib(2) fib(2) fib(1)
     / \     / \    / \
fib(2)fib(1)...

Notice:

fib(3)

is calculated twice

fib(2)

is calculated three times

fib(1)

many times

Lots of repeated work.

Time Complexity
O(2ⁿ)

Very slow.

DP Solution (Memoization)

Store answers.

def fib(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

    return memo[n]

Now:

fib(3)

computed once

↓

saved

↓

reused forever

Time becomes

O(n)

Huge improvement.

What is Memoization?

Memoization means:

Compute once

↓

Store answer

↓

Reuse later

It's simply a cache.

Bottom-Up DP (Tabulation)

Instead of recursion...

Build answers from the bottom.

We know:

F(0)=0

F(1)=1

Then

F(2)=1

F(3)=2

F(4)=3

F(5)=5

Python:
"""

def fib(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)

    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

"""
Again

O(n)

Memoization vs Tabulation
| Memoization     | Tabulation           |
| --------------- | -------------------- |
| Top-down        | Bottom-up            |
| Uses recursion  | Uses loops           |
| Cache results   | Build a table        |
| Easier to write | Often more efficient |
Both are Dynamic Programming.

Example 2: Climbing Stairs

Problem

You can climb

1 step
2 steps

How many different ways to climb 5 stairs?

Let's compute.

1 stair

1 way
2 stairs

1+1

2

↓

2 ways

3 stairs

1+1+1

1+2

2+1

↓

3 ways

Notice something?

Ways(3)

=

Ways(2)

+

Ways(1)

Exactly Fibonacci!

Python
"""

def climb(n):
    if n <= 2:
        return n

    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

"""
Example 3: House Robber
Interview favorite.

You have houses:

[2, 7, 9, 3, 1]

Can't rob adjacent houses.

Maximum money?

Choices

2

↓

7

↓

9

↓

3

↓

1

At every house

Two options.

Rob it

or

Skip it

DP remembers

Best answer up to house i

instead of recalculating.

Recognizing DP Problems

Interview clues

Maximum...
Minimum...
Number of ways...
Longest...
Cheapest...
Can you reach...
Optimal solution...

If the problem asks for the best, minimum, maximum, 
or number of ways, there's a good chance DP is involved.

Common Interview DP Problems

Easy

Fibonacci
Climbing Stairs
Min Cost Climbing Stairs

Medium

House Robber
Coin Change
Longest Increasing Subsequence
Partition Equal Subset Sum
Unique Paths

Hard

Edit Distance
Longest Common Subsequence
Regular Expression Matching
Burst Balloons

The 5-Step DP Recipe

Whenever you face a DP problem, follow this process:

1. Define the state

Ask:

"What does dp[i] represent?"

Examples:

dp[i]

=

Maximum money until house i

or

dp[i]

=

Number of ways to reach stair i

2. Find the recurrence relation

Ask:

"How can I compute the current answer using previous answers?"

Example:

dp[i]

=

dp[i-1]

+

dp[i-2]

3. Define the base cases

Example:

dp[0]=0

dp[1]=1

4. Compute all states

Usually with a loop.

5. Return the final answer

Usually:

dp[n]

Dynamic Programming vs Recursion
| Recursion                | Dynamic Programming             |
| ------------------------ | ------------------------------- |
| May repeat the same work | Reuses previous results         |
| Can be exponential       | Often linear or polynomial      |
| Uses function calls      | Uses memoization or tables      |
| Simpler but slower       | Slightly more code, much faster |

Interview Roadmap

Congratulations! You've now covered nearly all of the core topics for software engineering interviews:

✅ Arrays & Strings
✅ Linked Lists
✅ Hash Maps
✅ Stacks & Queues
✅ Trees & Binary Trees
✅ Binary Search Trees
✅ Heaps / Priority Queues
✅ Graphs (BFS & DFS)
✅ Two Pointers
✅ Sliding Window
✅ Binary Search
✅ Recursion
✅ Dynamic Programming

These topics form the foundation of the vast majority of coding interview questions at major tech companies.

My recommendation for practice

Don't try to memorize dozens of DP solutions. Instead, master these five problems in order:

Fibonacci – learn memoization and tabulation.
Climbing Stairs – recognize the recurrence relation.
House Robber – optimize decisions over a sequence.
Coin Change – build solutions from smaller amounts.
Longest Common Subsequence – introduce 2D DP tables.

If you can confidently solve and explain these, 
you'll have learned the core patterns that appear 
in many other Dynamic Programming interview questions.
"""

