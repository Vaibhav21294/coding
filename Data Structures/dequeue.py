from collections import deque

# Initialize deque
dq = deque()

# Add elements to both ends
dq.append(10)       # add to right
dq.appendleft(20)   # add to left
dq.append(30)       # add to right
print("Deque after additions:", dq)   # deque([20, 10, 30])

# Remove elements from both ends
right = dq.pop()        # remove from right
left = dq.popleft()     # remove from left
print("Removed right:", right)   # 30
print("Removed left:", left)     # 20
print("Deque after removals:", dq)   # deque([10])

# Peek both ends
print("Front element:", dq[0])   # 10
print("Rear element:", dq[-1])   # 10
