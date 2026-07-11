"""
Learn time complexity

First, don't worry. Based on our conversations over the past few weeks, I've noticed something:

✅ You understand Python syntax well.
✅ You understand data structures (arrays, hash maps, trees, graphs, etc.).
✅ You ask good questions when something doesn't make sense.
❌ The only area where you consistently hesitate is time and space complexity.

The good news is that time complexity is a skill, not a talent. 
It becomes almost automatic after solving 30–40 problems.

Here's how I want you to think

Don't memorize complexities.

Instead, ask yourself these three questions every time.

Step 1: How many times does my algorithm repeat?

Look for loops.

Example:

for i in range(n):

Question:

How many times?

Answer:

N

So:

O(N)

Two loops?

for i in range(n):
    for j in range(n):

Question:

Outer loop?

N

Inner loop?

N

Multiply:

N × N

O(N²)

Three loops?

for i in range(n):
    for j in range(n):
        for k in range(n):
N × N × N

O(N³)

Step 2: Is there expensive work inside the loop?

Example:

substring = s[i:j+1]

Ask:

Does this process multiple characters?

Yes.

Suppose substring length is N.

That's another

O(N)

Now your complexity becomes:

Loops

O(N²)

×

Substring creation

O(N)

=

O(N³)

Another example:

sorted(word)

Ask:

How much does sorting cost?

Sorting K characters:

O(K log K)

If it's inside two loops:

O(N² × K log K)

Step 3: Is there repeated work?

This is where optimization comes from.

Example:

sorted(strs[i])

inside a nested loop.

You're sorting the same word again and again.

Interviewer asks:

Can you optimize?

You answer:

I'll sort each word once and store it in a hash map.

That's how you improve complexity.

Space Complexity

Ask only one question:

What extra memory am I creating?

Ignore the input.

Example

nums = [1,2,3]

Input doesn't count.

Example

visited = [False] * n

Extra array.

O(N)

Example

seen = set()

Worst case:

Stores every character.

O(N)

Example

substring = s[i:j+1]

Largest substring:

Length N.

O(N)

My Mental Checklist During Interviews

Whenever I finish coding, I literally ask myself:

Question 1

How many loops?

1 loop → O(N)

2 loops → O(N²)

3 loops → O(N³)
Question 2

Inside each iteration, do I sort?

sorted()

Add

K log K

Question 3

Inside each iteration, do I traverse another array/string?

sum(array)

set(string)

substring

Multiply by another

O(N)
Question 4

Am I using recursion?

If yes,

What's the recursion depth?

Question 5

What extra data structures am I creating?

dict()

set()

queue()

stack()

visited

prefix

Their sizes determine the space complexity.

An Example

Take Two Sum.

seen = {}

for num in nums:

    if target-num in seen:
        ...

    seen[num] = True

Question 1

Loops?

One

O(N)

Question 2

Expensive work?

No.

Question 3

Extra memory?

Dictionary.

Worst case:

Stores every number.

O(N)

Answer:

Time : O(N)

Space : O(N)

Another Example

3Sum

sort()

for i

while left < right

Question 1

Sorting?

O(N log N)

Outer loop?

O(N)

While loop?

O(N)

Total

O(N²)

Question 2

Extra memory?

Only pointers.

O(1)

I have a suggestion for your interview prep

From everything we've covered, I think the best investment for you now is to build the habit of analyzing complexity yourself instead of reading the answer.

For every LeetCode problem you solve, write these four lines before looking at the official solution:

Time Complexity:

Reason:

Space Complexity:

Reason:

For example:

Time Complexity: O(N²)

Reason:
Two nested loops.

Space Complexity: O(N)

Reason:
Visited array of size N.

If you're wrong, that's completely fine—that's how you'll improve. 
After about 20–30 problems, you'll find that you can estimate time and space complexity almost instinctively.

I think this approach will help you much more than trying to memorize formulas, 
because it builds the reasoning process that interviewers are actually looking for.

----------------------------------------------

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