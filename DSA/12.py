class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next

            current.next = new_node
            new_node.next = self.head

    def display(self):
        if self.is_empty():
            print("Circular linked list is empty")
        else:
            current = self.head
            while True:
                print(current.data, end=" ")
                current = current.next
                if current == self.head:
                    break


# Test the CircularLinkedList
clist = CircularLinkedList()

# Insert elements into the circular linked list
clist.insert(1)
clist.insert(2)
clist.insert(3)
clist.insert(4)

# Display the circular linked list
clist.display()
