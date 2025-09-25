# queue_challenge.py

def meal_distribution_with_queue():
    from collections import deque
    queue = deque(["Student1", "Student2", "Student3", "Student4"])
    print("Meal Distribution Order (Queue):")
    while queue:
        student = queue.popleft()
        print(f"{student} receives meal")

def meal_distribution_with_stack():
    stack = ["Student1", "Student2", "Student3", "Student4"]
    print("Meal Distribution Order (Stack):")
    while stack:
        student = stack.pop()
        print(f"{student} receives meal")

print("--- Using Queue ---")
meal_distribution_with_queue()

print("\n--- Using Stack ---")
meal_distribution_with_stack()
