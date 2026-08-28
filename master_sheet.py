'''
Points

1. Create
2. Add, Remove
3. Iterate, Access
'''

######################################################################################

'''
Arrays, Strings, Hashsets, Hashmaps
| Operation        | Array / List     | String        | HashSet       | HashMap                 |
| ---------------- | ---------------- | ------------- | ------------- | ----------------------- |
| **Create**       | `nums = []`      | `s = ""`      | `s = set()`   | `d = {}`                |
| **Add**          | `nums.append(x)` | ❌ immutable   | `s.add(x)`    | `d[key] = value`        |
| **Remove**       | `nums.pop(i)`    | ❌ immutable   | `s.remove(x)` | `d.pop(key)`            |
| **Access**       | `nums[i]`        | `s[i]`        | ❌ no index    | `d[key]`                |
| **Iterate**      | `for x in nums:` | `for c in s:` | `for x in s:` | `for k,v in d.items():` |
| **Check exists** | `x in nums`      | `x in s`      | `x in s`      | `key in d`              |
| **Length**       | `len(nums)`      | `len(s)`      | `len(s)`      | `len(d)`                |
'''

######################################################################################

'''
Queue vs Stack
Queue vs Stack
| Operation       | Queue (`deque`) | Stack (`list`)    |
| --------------- | --------------- | ----------------- |
| **Create**      | `q = deque()`   | `stack = []`      |
| **Add**         | `q.append(x)`   | `stack.append(x)` |
| **Remove**      | `q.popleft()`   | `stack.pop()`     |
| **Access next** | `q[0]`          | `stack[-1]`       |
| **Iterate**     | `for x in q:`   | `for x in stack:` |
| **Check empty** | `if not q:`     | `if not stack:`   |
| **Length**      | `len(q)`        | `len(stack)`      |
'''

######################################################################################

'''
Linkedlist
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

| Operation        | Linked List                    |
| ---------------- | ------------------------------ |
| **Create node**  | `node = ListNode(5)`           |
| **Access value** | `node.val`                     |
| **Access next**  | `node.next`                    |
| **Add node**     | `node.next = new_node`         |
| **Remove node**  | `node.next = node.next.next`   |
| **Iterate**      | `while node: node = node.next` |
| **Check empty**  | `if not head:`                 |

# Most important traversal pattern
current = head

while current:
    print(current.val)
    current = current.next

node.val          # get value
node.next         # get next node
node = node.next  # move forward
'''

######################################################################################

"""
Binary tree
A binary tree is a data structure where each node can have at most 2 children:

a left child
a right child

For example:

        1
       / \
      2   3
     / \
    4   5

Here:

1 is the root
2 and 3 are children of 1
4 and 5 are children of 2
3, 4, and 5 have no children → they are leaf nodes

Binary Tree — Cheat Sheet
In LeetCode, you usually get a TreeNode:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

| Operation              | Binary Tree             |
| ---------------------- | ----------------------- |
| **Create node**        | `node = TreeNode(5)`    |
| **Access value**       | `node.val`              |
| **Access left**        | `node.left`             |
| **Access right**       | `node.right`            |
| **Add left child**     | `node.left = new_node`  |
| **Add right child**    | `node.right = new_node` |
| **Remove left child**  | `node.left = None`      |
| **Remove right child** | `node.right = None`     |
| **Check empty**        | `if not root:`          |
| **Iterate / Traverse** | DFS / BFS               |

Remember
node.val       → value
node.left      → left child
node.right     → right child


DFS → recursion / stack
BFS → queue

The main thing to understand:

Linked List:
node → next


Binary Tree:
       node
      /    \
   left   rights
"""

######################################################################################

"""
DFS
        1
       / \
      2   3
     / \   \
    4   5   6

1. DFS

The code I gave was:
def dfs(node):
    if not node:
        return

    dfs(node.left)
    dfs(node.right)

The important thing

DFS is essentially:

1. Go into the node
2. Explore left
3. Explore right

For our tree, it visits:

1 → 2 → 4 → 5 → 3 → 6

DFS — Cheat Sheet
| Item               | Remember                             |
| ------------------ | ------------------------------------ |
| **Meaning**        | Go **deep first**                    |
| **Tree**           | `dfs(node.left)` → `dfs(node.right)` |
| **Implementation** | **Recursion / Stack**                |
| **Base case**      | `if not node: return`                |
| **Graph**          | Use `visited` set                    |

Core template
def dfs(node):
    if not node:
        return

    # process node

    dfs(node.left)
    dfs(node.right)

Memory:
DFS → Deep → Recursion/Stack
"""

######################################################################################

"""
BFS — Simple Explanation

BFS = Breadth First Search

Visit nodes level by level.

Example:
        1
       / \
      2   3
     / \   \
    4   5   6

BFS visits:

1 → 2 → 3 → 4 → 5 → 6

Think:

Level 1 → 1
Level 2 → 2, 3
Level 3 → 4, 5, 6

BFS uses a Queue because the first node added should be the first node processed.

BFS — Cheat Sheet
| Item               | Remember                    |
| ------------------ | --------------------------- |
| **Meaning**        | Go **level by level**       |
| **Data structure** | **Queue**                   |
| **Python**         | `deque`                     |
| **Add**            | `q.append(node)`            |
| **Remove**         | `q.popleft()`               |
| **Tree**           | No `visited` usually needed |
| **Graph**          | Usually use `visited`       |
| **Best for**       | Levels / shortest path      |
| **Time**           | `O(V)`                      |

Core Tree Template
from collections import deque

q = deque([root])

while q:
    node = q.popleft()

    if node.left:
        q.append(node.left)

    if node.right:
        q.append(node.right)

Remember

BFS → Level by level → Queue → deque → popleft()
"""

######################################################################################

"""
Heap — Simple Explanation

A heap is a non-linear tree-based data structure that maintains a special ordering property: 
in a Min Heap, the parent is ≤ its children; 
in a Max Heap, the parent is ≥ its children.

Example Min Heap:

        2
       / \
      5   8
     / \
    10  7
The smallest element is always at the root (2).

Memorize

Heap → Tree → Parent has priority over children → Min/Max at root → heapq in Python

And one important clarification: a heap is conceptually a complete binary tree, not a general graph. 
In Python, heapq stores that tree efficiently as a list.

A heap is a data structure that lets you quickly get the smallest or largest element.

For Python interviews, the most important thing to remember is:

Python's heapq is a Min Heap by default.

Example:

import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)

heapq.heappop(heap)   # 2

You don't need to keep the entire list sorted. 
The heap only guarantees that the smallest element is at the top.

Heap — Cheat Sheet
| Operation      | Python                     |
| -------------- | -------------------------- |
| **Create**     | `heap = []`                |
| **Add**        | `heapq.heappush(heap, x)`  |
| **Remove min** | `heapq.heappop(heap)`      |
| **Peek min**   | `heap[0]`                  |
| **Size**       | `len(heap)`                |
| **Build heap** | `heapq.heapify(nums)`      |
| **Min Heap**   | Default `heapq`            |
| **Max Heap**   | `heapq.heappush(heap, -x)` |

Complexity
| Operation  |       Time |
| ---------- | ---------: |
| `heappush` | `O(log n)` |
| `heappop`  | `O(log n)` |
| `heap[0]`  |     `O(1)` |
| `heapify`  |     `O(n)` |

Remember

Heap → quickly get min/max → heapq → Min Heap by default

"""

######################################################################################


"""
Two Pointers — Cheat Sheet

| Item                 | Remember                                  |
| -------------------- | ----------------------------------------- |
| **Idea**             | Use **2 indices** to scan an array/string |
| **Pointers**         | Usually `left`, `right`                   |
| **Move**             | `left += 1` / `right -= 1`                |
| **Common direction** | One from left, one from right             |
| **Best for**         | Sorted arrays, pairs, palindromes         |
| **Time**             | Usually `O(n)`                            |
| **Space**            | Usually `O(1)`                            |

Core template
left = 0
right = len(nums) - 1

while left < right:
    # process

    if condition:
        left += 1
    else:
        right -= 1

Remember

Two Pointers → left + right → move one/both pointers → usually O(n)
"""

######################################################################################

"""
Sliding Window — Cheat Sheet

| Item             | Remember                              |
| ---------------- | ------------------------------------- |
| **Idea**         | Maintain a **window** `[left, right]` |
| **Expand**       | `right += 1`                          |
| **Shrink**       | `left += 1`                           |
| **When shrink?** | When window violates the condition    |
| **Best for**     | **Contiguous** subarrays / substrings |
| **Time**         | Usually `O(n)`                        |
| **Space**        | Usually `O(1)` or `O(k)`              |

Core template
left = 0

for right in range(len(nums)):
    # add nums[right]

    while condition_is_invalid:
        # remove nums[left]
        left += 1

    # update answer

Remember

Sliding Window → Contiguous range → Expand right → Shrink left → usually O(n)
"""

######################################################################################

"""
Binary Search — Cheat Sheet
| Item          | Remember                                      |
| ------------- | --------------------------------------------- |
| **Idea**      | Search a **sorted** array by eliminating half |
| **Pointers**  | `left`, `right`                               |
| **Middle**    | `mid = (left + right) // 2`                   |
| **Too small** | `left = mid + 1`                              |
| **Too large** | `right = mid - 1`                             |
| **Time**      | `O(log n)`                                    |
| **Space**     | `O(1)`                                        |

Core template
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

return -1

Remember

Binary Search → Sorted → Check middle → Eliminate half → O(log n)
"""

######################################################################################

"""
Intervals — Cheat Sheet

| Item           | Remember                             |
| -------------- | ------------------------------------ |
| **Represent**  | `[start, end]`                       |
| **Sort**       | `intervals.sort(key=lambda x: x[0])` |
| **Overlap**    | `current_start <= previous_end`      |
| **No overlap** | `current_start > previous_end`       |
| **Merge**      | `end = max(end, current_end)`        |
| **Greedy**     | Often sort by **end**                |
| **Time**       | Usually `O(n log n)`                 |
| **Space**      | Usually `O(n)` for result            |

Core pattern

intervals.sort(key=lambda x: x[0])

for start, end in intervals:
    # compare with previous interval

Remember

Intervals → Sort → Compare start/end → Merge or choose greedily
"""

######################################################################################

"""
Greedy — Cheat Sheet

| Item                 | Remember                                 |
| -------------------- | ---------------------------------------- |
| **Idea**             | Make the **best choice now**             |
| **Goal**             | Local best → leads to global best        |
| **Typical approach** | Sort / scan → make a choice → never undo |
| **Backtracking?**    | ❌ No                                     |
| **DP?**              | ❌ Usually no                             |
| **Time**             | Often `O(n)` or `O(n log n)`             |

Core pattern
for x in items:
    if best_choice_now:
        # take it

Remember

Greedy → Best choice now → Don't reconsider → Usually simple one-pass logic
"""

######################################################################################
######################################################################################
######################################################################################
######################################################################################
######################################################################################

# 1. Arrays

nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

for i in range(len(nums)):
    print(nums[i])

"""
Syntax VariationsThe function accepts up to three integer arguments:

pythonrange(stop)
range(start, stop)
range(start, stop, step)

How Arguments Workstart (Optional): 
The first number in the sequence. 
Defaults to 0.stop (Required): The number where the sequence ends. 
The value is exclusive, meaning the sequence stops right before this number.step 
(Optional): The increment value between each number. Defaults to 1.
"""

for i in range(5):
    print(i, end=" ")
# Output: 0 1 2 3 4

for i in range(2, 6):
    print(i, end=" ")
# Output: 2 3 4 5

for i in range(0, 10, 2):
    print(i, end=" ")
# Output: 0 2 4 6 8

# 4. Reverse CountingTo count downwards, use a larger start value and a negative
for i in range(5, 0, -1):
    print(i, end=" ")
# Output: 5 4 3 2 1

nums = []                 # create

nums[i]                   # access
nums[-1]                  # last

for num in nums:          # iterate
    ...

for i, num in enumerate(nums):
    ...

nums.append(x)            # add
nums.pop()                # remove last
nums.pop(i)               # remove index

x in nums                 # search

len(nums)                 # size

nums[i:j]                 # slice

nums.sort()               # sort
nums.reverse()            # reverse

######################################################################################

# 2. Strings

name = "Vaibhav"

for char in name:
    print(char)

"""
V
a
i
b
h
a
v
"""

s = ""                         # create

s[i]                          # access
s[-1]                         # last

for char in s:                # iterate
    ...

for i, char in enumerate(s):
    ...

len(s)                        # size

char in s                     # search

s[i:j]                        # slice
s[::-1]                       # reverse

s.lower()
s.upper()

char.isalpha()
char.isdigit()
char.isalnum()

s.split()                     # string → list
"".join(chars)                # list → string

list(s)                       # string → list

######################################################################################

# 3. Hashsets

s = set()

s.add(x)          # add
s.remove(x)       # remove (error if absent)
s.discard(x)      # remove (no error if absent)

x in s            # check existence

for x in s:       # iterate
    ...

len(s)            # size

######################################################################################

# 4. Hashmaps

d = {}                         # create

d[key]                        # access

d[key] = value                # add / update

d.get(key)                    # get value
d.get(key, 0)                 # get with default

key in d                      # check if key exists

d[key] += 1                   # increment

d.pop(key)                    # remove

len(d)                        # size

for key in d:                 # iterate keys
    ...

for key, value in d.items():  # iterate key + value
    ...

for value in d.values():      # iterate values
    ...

d.keys()                      # all keys
d.values()                    # all values
d.items()                     # key-value pairs

######################################################################################

# 5. Queue

# Queue

# FIFO → First In, First Out

from collections import deque


q = deque()


q.append(1)
q.append(2)
q.append(3)


q.popleft()    # 1

'''
1 → 2 → 3
↑
removed first
'''

######################################################################################

# 6. Stack

# Stack

# LIFO → Last In, First Out

stack = []


stack.append(1)
stack.append(2)
stack.append(3)


stack.pop()    # 3

'''
1 → 2 → 3
        ↑
    removed first
'''

######################################################################################

# Linked List — Python Cheat Sheet

'''
Unlike Stack, Python doesn't have a built-in linked list. 
In LeetCode, you usually use the provided ListNode.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
| Operation            | Linked List                  |
| -------------------- | ---------------------------- |
| **Create node**      | `node = ListNode(5)`         |
| **Create link**      | `node.next = other`          |
| **Access value**     | `node.val`                   |
| **Access next**      | `node.next`                  |
| **Add after node**   | `node.next = new_node`       |
| **Remove next node** | `node.next = node.next.next` |
| **Iterate**          | `while node:`                |
| **Check empty**      | `if not head:`               |

Most important traversal pattern
current = head


while current:
    print(current.val)
    current = current.next

Add a node

Suppose:

1 → 2 → 3

Want to add 5 after 2:

new_node = ListNode(5)


new_node.next = node2.next
node2.next = new_node

Result:

1 → 2 → 5 → 3

Remove a node

To remove 2:

node1.next = node1.next.next

Result:

1 → 3

Memorize
Linked List


node.val       → value
node.next      → next node


current = head


while current:
    ...
    current = current.next

The biggest difference from an array:

Array       → nums[i]       → direct access
Linked List → node.next     → follow links

So accessing the i-th node in a linked list takes O(n), whereas array indexing is O(1).

The 3 things to memorize
node.val          # get value
node.next         # get next node
node = node.next  # move forward
"""

######################################################################################

# Binary Tree — Cheat Sheet
# In LeetCode, you usually get a TreeNode:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Binary Tree — Complete Cheat Sheet
| Operation              | Binary Tree             |
| ---------------------- | ----------------------- |
| **Create node**        | `node = TreeNode(5)`    |
| **Access value**       | `node.val`              |
| **Access left**        | `node.left`             |
| **Access right**       | `node.right`            |
| **Add left child**     | `node.left = new_node`  |
| **Add right child**    | `node.right = new_node` |
| **Remove left child**  | `node.left = None`      |
| **Remove right child** | `node.right = None`     |
| **Check empty**        | `if not root:`          |
| **Iterate / Traverse** | DFS / BFS               |
"""

"""
DFS
        1
       / \
      2   3
     / \   \
    4   5   6

1. DFS

The code I gave was:
def dfs(node):
    if not node:
        return

    dfs(node.left)
    dfs(node.right)

The important thing

DFS is essentially:

1. Go into the node
2. Explore left
3. Explore right

For our tree, it visits:

1 → 2 → 4 → 5 → 3 → 6
"""

######################################################################################

"""
BFS dry run
from collections import deque

q = deque([root])

while q:
    node = q.popleft()

    if node.left:
        q.append(node.left)

    if node.right:
        q.append(node.right)


Step 1

Start:

Queue: [1]

Take the first item:

node = q.popleft()
node = 1
Queue: []

Add 1's children:

Queue: [2, 3]

Step 2

Take the first item:

node = 2
Queue: [3]

Add 2's children:

Queue: [3, 4, 5]

Step 3

Take the first item:

node = 3
Queue: [4, 5]

3 has no children.

Queue stays:

[4, 5]

Step 4

Take 4:

node = 4
Queue: [5]

No children.

Step 5

Take 5:

node = 5
Queue: []

No children.

Queue is empty → stop.

Final BFS order
1 → 2 → 3 → 4 → 5
"""

######################################################################################

"""
Example: Max Heap

Python doesn't directly provide a max heap, so use negative values:

heap = []

heapq.heappush(heap, -5)
heapq.heappush(heap, -2)
heapq.heappush(heap, -8)

-heapq.heappop(heap)    # 8

So:

Min Heap → normal values
Max Heap → negative values

One more important interview pattern

For Top K Frequent Elements, you may see tuples:

heapq.heappush(heap, (frequency, num))

Python compares the first element of the tuple first:

(frequency, num)
     ↑
   priority

So the heap will remove the tuple with the smallest frequency first.
"""

######################################################################################