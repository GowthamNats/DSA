class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, head = None):
        self.head = head

    def insertAtEnd(self, data):
        new_node = Node(data)
        current = self.head

        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def insertAtBeginning(self, data):
        new_node = Node(data)
        current = self.head

        new_node.next = current
        self.head = new_node

    def insertAtPosition(self, data, position):
        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 1
        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of range.")
            return

        new_node.next = current.next
        current.next = new_node

    def deleteElement(self, data):
        current = self.head
        prev = None

        if current and current.value == data:
            self.head = current.next
            current = None
            return

        while current:
            if current.value == data:
                break
            prev = current
            current = current.next

        if not current:
            return

        prev.next = current.next
        current = None

    def printList(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next

    def search(self, key):
        current = self.head

        while current is not None:
            if current.value == key:
                return True
            current = current.next

        return False
    
    def sortLinkedList(self):
        current = self.head
        index = Node(None)

        if self.head is None:
            return
        else:
            while current is not None:
                index = current.next

                while index is not None:
                    if current.value > index.value:
                        current.value, index.value = index.value, current.value

                    index = index.next
                current = current.next

if __name__ == '__main__':
    ll = LinkedList()

    ll.insertAtEnd(1)
    ll.insertAtEnd(2)
    ll.insertAtEnd(3)
    ll.insertAtBeginning(4)
    ll.insertAtPosition(9, 2)
    ll.deleteElement(3)
    print(ll.search(2))
    ll.sortLinkedList()
    ll.printList()