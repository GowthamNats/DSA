# Queue Implementation
class Queue:
    def __init__(self, size):
        self.elements = []
        self.size = size

    def enqueue(self, data):
        if self.isFull():
            return "Stack Overflow"
        self.elements.append(data)

    def dequeue(self):
        if self.isEmpty():
            return "Stack Underflow"
        return self.elements.pop(0)
    
    def isEmpty(self):
        return len(self.elements) == 0
    
    def isFull(self):
        return len(self.elements) == self.size
    
    def printQueue(self):
        print(self.elements)

# Queue usage  
if __name__ == "__main__":
    queue = Queue(5)

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print(queue.isFull(), queue.isEmpty())

    print(queue.dequeue())

    queue.printQueue()
