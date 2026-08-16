"""
Pow(x, n) — LeetCode 50
Question

Given x and n, return:

xⁿ
Examples
Input:  x = 2, n = 3
Output: 8

Because:

2³ = 2 × 2 × 2 = 8

Recursive idea

Instead of multiplying x n times, we can divide the problem in half.

For example:

2⁸
= 2⁴ × 2⁴

2⁴
= 2² × 2²

2²
= 2¹ × 2¹

So we're repeatedly making the problem half as big.
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        half = self.myPow(x, n // 2)

        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
        
"""
Complexity

This is the important part compared with Fibonacci.

Every recursive call changes:

n → n / 2

So:

n
↓
n/2
↓
n/4
↓
n/8
↓
...
↓
1

For example, n = 16:

16 → 8 → 4 → 2 → 1 → 0

Only about log₂(n) levels.

Therefore:

Time: O(log n)

Space: O(log n) because the recursion stack has log n calls.
"""