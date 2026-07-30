"""
Remove Nth Node From End of List (LeetCode 19)

Category
Data Structure: Linked List
Pattern: Two Pointers (Fast & Slow)

Problem Statement

Given the head of a linked list, remove the nth node from the end of the list and return the head.

Example:

Input:
1 → 2 → 3 → 4 → 5
n = 2

Output:
1 → 2 → 3 → 5
"""

class Solution:
    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next

"""
Complexity

Time: O(n)

fast moves at most n + 1 steps.
slow moves at most n steps.

Overall:

O(2n) = O(n)

Space: O(1)

Interview Tip

This is one of the classic Fast & Slow Pointer problems.

Whenever a problem says:

"nth from the end"
"middle of the list"
"cycle"

you should immediately think:

Can I solve this by keeping two pointers a fixed distance apart?
"""