# Last In First Out (LIFO)

# Stack is list in Python, also you can use deque

# Using a list as a Stack

stack = []

stack.append('https://www.cnn.com/')
stack.append('https://www.cnn.com/world')
stack.append('https://www.cnn.com/india')
stack.append('https://www.cnn.com/china')

print(stack[-1])

# Using deque as a stack

from collections import deque
stack = deque()

dir(stack)

stack.append("https://www.cnn.com/")
stack.append("https://www.cnn.com/world")
stack.append("https://www.cnn.com/india")
stack.append("https://www.cnn.com/china")

stack.pop()

# Implement Stack class using a deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

s = Stack()
s.is_empty()
s.pop()
s.push(9)
s.push(34)
s.push(78)
s.peek()
