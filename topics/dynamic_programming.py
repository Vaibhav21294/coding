"""
What is Dynamic Programming?

Dynamic Programming = Save answers you've already calculated so you don't calculate them again.

That's it.

Example: Climbing Stairs

Suppose:

n = 5

The brute force recursion looks like this:
dfs(5)
├── dfs(4)
│   ├── dfs(3)
│   │   ├── dfs(2)
│   │   └── dfs(1)
│   │
│   └── dfs(2)   <-- Again!
│
└── dfs(3)       <-- Again!
    ├── dfs(2)
    └── dfs(1)

Notice:

dfs(3)

is calculated twice.

dfs(2)

is calculated three times.

We're doing the same work over and over.

DP says:

Instead of doing

dfs(3)

again...

just remember its answer.

dfs(3)

↓

3 ways

Store it.

Next time someone asks

dfs(3)

don't calculate it.

Just return

3

Real Life Analogy

Imagine your teacher asks

What is 25 × 17?

You calculate it.

425

Five minutes later your friend asks the same thing.

Would you multiply again?

No.

You remember

25 × 17 = 425

Dynamic Programming is exactly that.

Another Example

Suppose

n = 5

How many ways to reach stair 5?

Think backwards.

To reach stair 5, where could you come from?

4

or

3

So

Ways(5)
=
Ways(4)
+
Ways(3)

Similarly,

Ways(4)
=
Ways(3)
+
Ways(2)

Notice

Ways(3)

appears twice.

That's repeated work.

DP stores it once.

Bottom-Up DP

Instead of starting from the top,

start from the bottom.

Ways(1) = 1
Ways(2) = 2

Now calculate

Ways(3) = 3
Ways(4) = 5
Ways(5) = 8

Just keep filling the table.

Stair      Ways

1            1
2            2
3            3
4            5
5            8

Done.

The Three Signs of DP

Whenever you see a problem, ask yourself:

1. Can I break it into smaller problems?
Ways(5)

↓

Ways(4)
Ways(3)

✅ Yes

2. Are the same subproblems solved repeatedly?
Ways(3)
Ways(3)
Ways(3)

✅ Yes

3. Can I save the answers?
Ways(3) = 3

Store it.

✅ Yes

If all three are true...

Think Dynamic Programming.

My Simple Definition (the one I'd remember)

Recursion explores possibilities. Dynamic Programming avoids repeating the same work by saving answers.

One thing to notice

You've already learned Backtracking (Subsets).

Backtracking asks:

"What are all the possible choices?"

Dynamic Programming asks:

"How can I reuse the answer to a smaller problem?"

That's the biggest mental difference.

Backtracking → Explore every possibility.
Dynamic Programming → Reuse previous results to avoid repeated work.

I actually think Climbing Stairs is the perfect first DP problem 
because it introduces this idea without any complicated state or formulas. 
Once this clicks, problems like House Robber, Coin Change, and Longest Increasing Subsequence 
become much easier to understand.
"""