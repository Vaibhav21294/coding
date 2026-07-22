"""
Problem

Given two strings s and t, return True if t is an anagram of s, otherwise return False.

An anagram contains the same characters with the same frequencies, just in a different order.

Example
Input:
s = "anagram"
t = "nagaram"

Output:
True
Input:
s = "rat"
t = "car"

Output:
False
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashmap1 = {}
        hashmap2 = {}

        for char in s:
            if char not in hashmap1:
                hashmap1[char] = 1
            else:
                hashmap1[char] += 1

        for char in t:
            if char not in hashmap2:
                hashmap2[char] = 1
            else:
                hashmap2[char] += 1
            
        if hashmap1 == hashmap2:
            return True
        else:
            return False
        
"""
Complexity
Time: O(n)
Space: O(n)
"""