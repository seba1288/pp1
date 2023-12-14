#####
# Stack definition
##

stack = []

# add value at the top of the stack
def push(value):
    stack.append(value)
    
# remove the topmost element of the stack
# and return its value    
def pop():
    if not empty():
        return stack.pop()
    else:
        return None
    
# return true if the stack is empty
def empty():
    return len(stack) == 0

# display stack
def display():
    for i in range(len(stack)-1,-1,-1):
        print(stack[i])
    print()

#########################################

push(5)
push(3)
push(7)
display()
pop()
display()
pop()
display()

