# Stack implementation using list
stack = []

# Push elements (insert at end)
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after pushes:", stack)  # [10, 20, 30]

# Pop element (remove from end)
top = stack.pop()
print("Popped element:", top)        # 30
print("Stack after pop:", stack)     # [10, 20]

# Peek (see top element)
print("Top element:", stack[-1])     # 20
