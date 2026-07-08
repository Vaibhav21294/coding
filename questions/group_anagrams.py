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

Brute Force
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        visited = [False] * len(strs)

        for i in range(len(strs)):
            if visited[i]:
                continue
            
            visited[i] = True

            group = []
            group.append(strs[i])
            
            for j in range(i+1, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    visited[j] = True
                    group.append(strs[j])
            result.append(group)  
        return result     

"""
Total Time
O(N²) × O(K log K)

So the final time complexity is:

O(N² × K log K)

Space Complexity

Let's count the extra memory used.

visited
visited = [False] * len(strs)

Stores one boolean per string.

O(N)
group

At worst, all strings are anagrams.

group = ["eat","tea","ate", ...]

Stores up to N string references.

O(N)
result

This is the required output.

In interviews, the returned output is usually not counted as extra space.

Final Space Complexity

Auxiliary (extra) space:

O(N)

because of the visited array (and group, which is at most O(N) during one iteration).

If you include the output (result):

O(N)

since every input string appears exactly once in the output groups.

Interview Rule

When analyzing output space, ask yourself:

"Am I storing each element once, or am I duplicating elements?"

Stored once → O(N)
Duplicated many times → could become O(N²) or more
"""