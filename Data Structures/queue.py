"""

What is a Queue?

A Queue follows the rule:

First In, First Out (FIFO)

Think of people waiting in line at a coffee shop.

Front                          Back

Alice → Bob → Charlie

The first person who entered the line (Alice) is served first.

You join at the back.

You leave from the front.

Queue Operations

There are only two main operations.

1. Enqueue (Add)

Add to the back.

Queue:

[]

Add 3

[3]

Add 9

[3, 9]

Add 20

[3, 9, 20]

2. Dequeue (Remove)

Remove from the front.

Current queue:

Front

↓

[3, 9, 20]

Remove:

3

Queue becomes:

[9,20]

Remove again:

9

Queue becomes:

[20]

Notice:

We always remove the oldest element.

Python Queue

Python provides an efficient queue using deque.

from collections import deque

queue = deque()

Initially:

[]

Add to the queue
queue.append(3)

Queue:

[3]
queue.append(9)

Queue:

[3,9]
queue.append(20)

Queue:

[3,9,20]

Remove from the queue
queue.popleft()

Returns:

3

Queue becomes:

[9,20]

Another:

queue.popleft()

Returns:

9

Queue becomes:

[20]

Why not use a list?

You might think:

queue = []

Then:

queue.append(3)
queue.append(9)
queue.append(20)

Works fine.

But to remove from the front:

queue.pop(0)

Python must shift every remaining element one position to the left.

Example:

Before:

[3,9,20]

After removing 3:

[9,20]

Python has to move:

9 ←

20 ←

This shifting costs:

O(N)

With deque:

queue.popleft()

Nothing needs to shift.

It simply removes the first element.

Cost:

O(1)

That's why interviewers expect:

from collections import deque

Now let's connect this to BFS

Tree:

        3
       / \
      9   20
         / \
        15  7

Initially:

queue = deque([3])

Queue:

[3]

Remove the front:

node = queue.popleft()

Returns:

3

Queue:

[]

Now add its children:

queue.append(9)
queue.append(20)

Queue:

[9,20]

Next iteration:

Remove:

queue.popleft()

Returns:

9

Queue:

[20]

9 has no children.

Nothing added.

Next iteration:

Remove:

20

Queue:

[]

Now add:

queue.append(15)
queue.append(7)

Queue:

[15,7]

See the pattern?

Visit one node

↓

Add its children

↓

Visit next node

↓

Add its children

↓

Continue

This is exactly how Breadth-First Search (BFS) works.

One thing to notice

The queue is not storing numbers.

It's storing TreeNode objects.

When we write:

queue = deque([root])

it's actually storing the root node itself.

Then:

node = queue.popleft()

node is a TreeNode, so you can access:

node.val
node.left
node.right

Queue Cheat Sheet
| Operation         | Python         | Complexity |
| ----------------- | -------------- | ---------- |
| Create            | `deque()`      | O(1)       |
| Add to back       | `append(x)`    | O(1)       |
| Remove from front | `popleft()`    | O(1)       |
| Check if empty    | `while queue:` | O(1)       |
| Size              | `len(queue)`   | O(1)       |

I have a question for you

Suppose we execute:

from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print(queue.popleft())

queue.append(40)

print(queue.popleft())

print(queue)

Without running the code, what do you think the output will be? This is a great way to check if the queue concept has clicked.

[30, 40]

Very close! You got the final queue almost right, but let's execute it step by step.

from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

Queue is now:

Front

↓

[10, 20, 30]
First popleft()
print(queue.popleft())

Removes the front element.

Prints:

10

Queue becomes:

[20, 30]
Append 40
queue.append(40)

Queue:

[20, 30, 40]
Second popleft()
print(queue.popleft())

Removes:

20

Prints:

20

Queue becomes:

[30, 40]
Print queue
print(queue)

Prints:

deque([30, 40])
Final Output
10
20
deque([30, 40])

You correctly identified the final contents of the queue as [30, 40]. 
The only thing you missed was that the two popleft() calls each return the removed element, so they print 10 and 20 before the final queue.

I think you've understood queues now. 🎉

The only remaining piece for Binary Tree Level Order Traversal is understanding this line:

level_size = len(queue)

This is the part that almost everyone finds tricky at first, but once it clicks, you'll be able to solve almost every BFS tree problem. 
I can explain it with an animation-style dry run that shows the queue changing after every operation.


-------------------------------------

"""

from collections import deque

# Initialize queue
queue = deque()

# Enqueue elements (add to right)
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue after enqueues:", queue)  # deque([10, 20, 30])

# Dequeue element (remove from left)
front = queue.popleft()
print("Dequeued element:", front)      # 10
print("Queue after dequeue:", queue)   # deque([20, 30])

# Peek (see front element)
print("Front element:", queue[0])      # 20
