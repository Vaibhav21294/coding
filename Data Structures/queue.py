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
