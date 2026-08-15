"""
Fibonacci Number — LeetCode 509
Question

The Fibonacci numbers are defined as:

F(0) = 0
F(1) = 1

For every n > 1:

F(n) = F(n - 1) + F(n - 2)

Given n, return F(n).
"""

class Solution:
    def fib(self, n: int) -> int:

        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)

"""
Simple memory trick

For this recursive Fibonacci:

Time  → O(2^n)
        Two recursive calls → grows exponentially

Space → O(n)
        Deepest call chain → n

So for your notes, I'd write:

Time: O(2^n) — each call creates 2 more calls.
Space: O(n) — recursion can go n levels deep.
"""