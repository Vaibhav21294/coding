"""
My tips

1. Always do brute force first. Atleast I have one solution by now

2. Dry run data structure questions before implementing code

3. When you see code like this:
for i in range(n):
    for j in range(i + 1, n):
    
a quick mental shortcut is:

"I'm comparing every pair of elements exactly once."

The number of unique pairs in a collection of n items is:

n(n - 1) / 2

and that simplifies to O(n²).

4. visited = [False] * len(strs)

5. 
word = "cba"
sorted_word = sorted(word)
print(sorted_word) # ['a', 'b', 'c']
ans = "".join(sorted_word)
print(ans) # abc

6. 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        groups = defaultdict(list)

        for str in strs:
            key = "".join(sorted(str))
            groups[key].append(str)
        return list(groups.values())
"""