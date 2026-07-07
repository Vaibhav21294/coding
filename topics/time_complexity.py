"""
why is the below O(n^2) time complexity

strs = ["eat","tea","tan","ate","nat","bat"]

for i in range(len(strs)):
    for j in range(i+1, len(strs)):
        print(strs[i], strs[j])

This is a fantastic question because it gets to the heart of understanding nested loops and time complexity.

Let's analyze it step by step.

strs = ["eat","tea","tan","ate","nat","bat"]

for i in range(len(strs)):
    for j in range(i+1, len(strs)):
        print(strs[i], strs[j])

Here,

n = 6

because there are 6 words.

Let's count the iterations
i = 0
j = 1,2,3,4,5

Iterations:

5

Prints:

eat tea
eat tan
eat ate
eat nat
eat bat
i = 1
j = 2,3,4,5

Iterations:

4

Prints:

tea tan
tea ate
tea nat
tea bat
i = 2
j = 3,4,5

Iterations:

3
i = 3

Iterations:

2
i = 4

Iterations:

1
i = 5

Iterations:

0
Total iterations
5 + 4 + 3 + 2 + 1
=
15
Generalizing

If there are n elements, the total number of iterations is:

(n-1) + (n-2) + (n-3) + ... + 2 + 1

This is the sum of the first n-1 natural numbers.

The formula is:

n(n-1) / 2

For example, if n = 6:

6 × 5 / 2

= 15

Exactly what we counted.

Big-O Analysis

We ignore constants and lower-order terms.

n(n-1)/2

= (n² - n)/2

Ignoring /2 and -n:

O(n²)
Visual Triangle

The iterations form a triangle:

i=0  *****
i=1  ****
i=2  ***
i=3  **
i=4  *
i=5

Or numerically:

5
4
3
2
1

Total:

15

As n grows, this triangular pattern grows proportionally to n², which is why the time complexity is O(n²).

Why isn't it exactly n × n?

Notice the inner loop gets shorter every time:

Outer Loop     Inner Loop

0              n-1
1              n-2
2              n-3
...

So it's not exactly n × n iterations.

However:

n(n-1)/2

and

n²

grow at the same rate as n becomes large.

That's why in Big-O notation we write:

O(n²)

Interview Tip

When you see code like this:

for i in range(n):
    for j in range(i + 1, n):

a quick mental shortcut is:

"I'm comparing every pair of elements exactly once."

The number of unique pairs in a collection of n items is:

n(n - 1) / 2

and that simplifies to O(n²).

This pattern appears frequently in brute-force solutions for problems like:

Group Anagrams (pairwise comparison approach)
Two Sum (brute force)
Detecting duplicate pairs
Many graph algorithms that compare every pair of nodes

"""