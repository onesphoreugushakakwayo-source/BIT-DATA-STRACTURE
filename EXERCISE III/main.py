# main.py

from collections import deque

# === STACK ===
print("STACK:")

# MoMo Example
stack = ["Enter PIN", "Select Service", "Confirm"]
print("MoMo stack:", stack)
stack.pop()  # Undo last
print("After undo:", stack)

# UR Assignments
stack = ["AssignmentA", "AssignmentB", "AssignmentC"]
print("UR Assignments:", stack)
stack.pop()
stack.pop()
print("After popping two:", stack)

# Reverse string
text = "DATASTRUCTURE"
stack = list(text)
reversed_text = ''
while stack:
    reversed_text += stack.pop()
print("Reversed:", reversed_text)

# Stack Reflection
print("Stack Reflection: Stack is LIFO, like undo or temporary memory.\n")

# === QUEUE ===
print("QUEUE:")

# RRA Clients
queue = deque(["Client1", "Client2", "Client3", "Client4", "Client5", "Client6", "Client7", "Client8"])
for _ in range(3):
    queue.popleft()
print("RRA front after 3 served:", queue[0])

# BK ATM
queue = deque(["Client1", "Client2", "Client3", "Client4", "Client5", "Client6", "Client7"])
print("BK ATM last client:", queue[-1])

# Meal distribution
print("Meal Distribution: Queue is better (FIFO) for fairness.\n")

# Queue Reflection
print("Queue Reflection: FIFO is fair in schools — first come, first served.")
