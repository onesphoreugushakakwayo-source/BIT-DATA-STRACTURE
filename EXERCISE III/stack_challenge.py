# stack_challenge.py

def reverse_string_using_stack(input_string):
    stack = []

    # Step 1: Push each character into the stack
    for char in input_string:
        stack.append(char)

    # Step 2: Pop characters from stack to reverse the string
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string

original = "DATASTRUCTURE"
reversed_result = reverse_string_using_stack(original)
print("Original String:", original)
print("Reversed String:", reversed_result)
