# Stack Implementation
class Stack:
    def __init__(self, size) -> None:
        self.elements = []
        self.size = size

    def push(self, data):
        if self.isFull():
            return "Stack Overflow"
        self.elements.append(data)

    def pop(self):
        if self.isEmpty():
            return "Stack Underflow."
        return self.elements.pop() 

    def peek(self):
        return self.elements[-1] if ~self.isEmpty() else "Stack Empty."
    
    def isEmpty(self):
        return len(self.elements) == 0
    
    def isFull(self):
        return len(self.elements) == self.size
    
    def size(self):
        return self.size

    def printStack(self):
        print(self.elements)

# Stack Usage
if __name__ == '__main__':
    stack = Stack(5)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack.isEmpty(), stack.isFull())

    print(stack.peek())

    print(stack.pop())

    stack.printStack()
