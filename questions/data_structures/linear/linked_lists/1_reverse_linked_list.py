"""
Problem

Given

1 → 2 → 3 → 4 → 5

Return

5 → 4 → 3 → 2 → 1

Remember:

A linked list node is

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

Each node stores:

value
pointer to the next node
"""

class Solution:
    def reverseList(self, head):

        prev = None
        current = head

        while current:

            next_node = current.next

            current.next = prev

            prev = current

            current = next_node

        return prev
    
"""
Dry Run

Input

1 → 2 → 3

Initially

prev = None

current = 1

After first iteration

1 → None

prev = 1

current = 2

After second

2 → 1 → None

prev = 2

current = 3

After third

3 → 2 → 1

current = None

Loop ends.

Return

prev

which is

3

the new head.

Complexity

Each node is visited once.

Time
O(n)
Space
O(1)
"""