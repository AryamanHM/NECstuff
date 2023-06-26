class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_reverse_linked_list(head):
    if head is None:
        return

    # Recursively call the function for the next node
    print_reverse_linked_list(head.next)

    # Print the data of the current node
    print(head.data, end=" ")


# Test the function
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original Linked List:")
current = head
while current:
    print(current.data, end=" ")
    current = current.next

print("\nReverse Linked List:")
print_reverse_linked_list(head)
