"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Instead of copying everything, both lists are already sorted.

We can merge them exactly like the merge step of Merge Sort.

Idea

Compare the current nodes.

Choose the smaller node.

Move that list's pointer.

Repeat until one list finishes.

Example
list1: 1 → 2 → 4
        ↑

list2: 1 → 3 → 4
        ↑

Create a dummy node.

dummy
  |
  v
None
"""

class Solution:
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()
        tail = dummy

        while list1 and list2:

            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
    
"""
Complexity

Time: O(m + n)

Each node is visited exactly once.

Space: O(1)

We reuse the existing nodes.
We only create one dummy node.

This is one of the most confusing parts of linked list problems.

The answer is No, because we're not creating new nodes (except for one dummy node).
"""