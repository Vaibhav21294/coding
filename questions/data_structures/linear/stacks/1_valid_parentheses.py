"""

That's exactly how a stack (LIFO) works.

Problem

Given a string containing:

(
)
[
]
{
}

Determine if every opening bracket has the correct closing bracket in the correct order.

Example:

s = "()[]{}"

Output:
True

Example:

s = "(]"

Output:

False

Example:

s = "([)]"

Output:

False

Example:

s = "{[]}"

Output:

True
"""

class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"}":"{", "]":"[", ")":"("}

        stack = []

        for char in s:
            if char in hashmap.keys():
                if len(stack) == 0:
                    return False 
                if hashmap[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        
        if len(stack) != 0:
            return False
        else:
            return True

"""
Complexity
Time

You iterate through the string once.

Each character is:

pushed once
popped once

Time: O(n)

Space

In the worst case

((((((((

everything is pushed onto the stack.

Space: O(n)

1. Hash Map

Your hash map always has exactly 3 entries.

{
    ")": "(",
    "]": "[",
    "}": "{"
}

Whether the input is:

()

or

(((((((((((((((((((((((((((((

the hash map is still:

3 elements

It does not grow with the input size.

So its space is:

O(1)

This is called constant space.

2. Stack

Now suppose:

s = "((((((((("

As you scan the string:

(

Stack:

[
(
]

Next:

(

Stack:

[
(,
(
]

Eventually:

[
(,
(,
(,
(,
(,
(,
(
]

The stack size grows with the length of the input.

If the string has n opening brackets:

(((((((((((((

The stack stores:

n

elements.

So:

O(n)

Total Space

Hash map:

O(1)

Stack:

O(n)

Total:

O(1) + O(n)

In Big-O, we keep only the dominant term:

O(n)

General Rule

Suppose you have:

Array of size n
Hash map of size n
Stack of size n

Total:

O(n + n + n)

Simplifies to:

O(n)

Interview Tip

When analyzing space complexity, always ask:

"Can this data structure grow as the input grows?"

Yes → Include it in the complexity (e.g., O(n)).
No (fixed size regardless of input) → It's O(1).

In your solution:

mapping → O(1) ✅
stack → O(n) ✅

So the overall space complexity is O(n).
"""