class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    if head is None:
        return head

    current = head
    unique_elements = set([current.data])  # Set to store unique elements

    while current.next:
        if current.next.data in unique_elements:
            current.next = current.next.next  # Skip duplicate element
        else:
            unique_elements.add(current.next.data)
            current = current.next

    return head


def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()


# Test the program
# Create a linked list with duplicates: 1 -> 2 -> 3 -> 2 -> 4 -> 3
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(3)

print("Original Linked List:")
print_linked_list(head)

head = remove_duplicates(head)

print("Linked List after removing duplicates:")
print_linked_list(head)
