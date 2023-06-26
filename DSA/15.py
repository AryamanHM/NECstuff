class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_loop(head):
    if head is None or head.next is None:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True

        slow = slow.next
        fast = fast.next.next

    return False


# Test the program
# Create a linked list with a loop: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (loop)
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next.next  # Create a loop

if has_loop(head):
    print("Loop detected in the linked list")
else:
    print("No loop detected in the linked list")
