stack = []

def is_empty():
    return len(stack) == 0

def push(item):
    stack.append(item)

def popcheck():
    if not is_empty():
        return stack.pop()      #removes the value from the top of stack (stack follows LIFO)
    else:
        print("Stack is empty. Cannot pop.")

def peek():     #Shows top value of the stack without removing it.
    if not is_empty():
        return stack[-1]
    else:
        print("Stack is empty. Cannot peek.")

def size():
    return len(stack)

length1=int(input("Enter the number of elements you'd like to add: "))
for i in range(0, length1):
    push(int(input('Enter number: ')))

print("Stack:", stack)

popped_item = popcheck()
print("Popped item:", popped_item)
print("Stack after pop:", stack)

peeked_item = peek()
print("Peeked item:", peeked_item)

print("Stack size:", size())
