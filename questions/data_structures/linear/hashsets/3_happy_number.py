"""
Problem

A happy number is defined as:

Starting with a number:

Replace the number by the sum of the squares of its digits.
Repeat until:
The number becomes 1 → Happy number ✅
It enters a cycle → Not happy ❌

Example:

19

Process:

1² + 9² = 82

8² + 2² = 68

6² + 8² = 100

1² + 0² + 0² = 1

So:

19 is happy
"""

class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        while n != 1:

            if n in seen:
                return False

            seen.add(n)

            total = 0

            while n > 0:
                digit = n % 10
                total += digit * digit
                n = n // 10

            n = total

        return True
    
"""
Complexity

Let:

n = original number
d = number of digits

Each transformation processes the digits.

Time:

O(log n)

because number of digits is log10(n).

Space:

O(log n)

because we store the numbers in the cycle.
"""