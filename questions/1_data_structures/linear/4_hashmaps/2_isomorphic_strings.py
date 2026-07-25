"""
Problem

Two strings are isomorphic if you can replace every character in s with a character in t.

Rules:

Every character in s maps to exactly one character in t.
No two different characters in s can map to the same character in t.

Example 1
s = "egg"
t = "add"

Mapping:

e → a
g → d

Result:

True

Example 2
s = "foo"
t = "bar"

Mapping:

f → b
o → a

But later:

o → r

Now o maps to both a and r.

Return:

False

Example 3
s = "badc"
t = "baba"

You could try:

b → b
a → a
d → b

Now:

b → b
d → b

Two different characters map to the same character.

Invalid.

Better Solution (Hash Maps)

Instead of repeatedly checking previous characters, remember the mappings.

Suppose

s = "egg"
t = "add"

Read one character at a time.

Why do we need two hash maps?

Consider:

s = "ab"
t = "aa"

Using only one map:

a → a
b → a

This looks okay if you only check s → t.

But it's invalid because two different characters (a and b) map to the same character (a).

So we also store:

a ← a

Now when we try:

b → a

we notice:

a is already mapped from another character.

Return False.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):

            if s[i] in s_to_t:

                if s_to_t[s[i]] != t[i]:
                    return False

            else:
                s_to_t[s[i]] = t[i]

            if t[i] in t_to_s:

                if t_to_s[t[i]] != s[i]:
                    return False

            else:
                t_to_s[t[i]] = s[i]

        return True

"""
Complexity

We scan the strings once.

Time: O(n)
Space: O(n)
"""