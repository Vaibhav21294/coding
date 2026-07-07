"""
Group Anagrams is one of the most common Hash Map interview problems. 
The key insight is finding a way to identify that two words are anagrams.

Problem Statement

Given an array of strings strs, group the anagrams together.

You can return the answer in any order.

Example
Input:
strs = ["eat","tea","tan","ate","nat","bat"]

Output:
[
  ["eat","tea","ate"],
  ["tan","nat"],
  ["bat"]
]

Notice:

eat
tea
ate

All contain the same letters.

So they belong in one group.

What is an Anagram?

Two words are anagrams if they contain the same letters with the same frequency.

Examples:

listen
silent
evil
vile

Not anagrams:

eat
cat

Brute Force Solution

Compare every string with every other string.

To check if two strings are anagrams:

Sort both strings.
Compare them.
eat -> aet

tea -> aet

They match.

Time Complexity

Comparing every pair:

O(n²)

Sorting each string (length = k):

O(k log k)

Overall:

O(n² × k log k)

Too slow.
"""