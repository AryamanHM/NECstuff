class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    # Initialize three pointers: current, previous, and next_node
    current = head
    previous = None

    while current:
        # Store the next_node before modifying the current node's next pointer
        next_node = current.next

        # Reverse the link by pointing the current node's next to the previous node
        current.next = previous

        # Move the previous and current pointers one step forward
        previous = current
        current = next_node

    # Update the head pointer to the last node, which becomes the new head of the reversed list
    head = previous

    return head


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

# Reverse the linked list
head = reverse_linked_list(head)

print("\nReversed Linked List:")
current = head
while current:
    print(current.data, end=" ")
    current = current.next
