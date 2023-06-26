class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_center_element(head):
    slow = head
    fast = head

    # Move the fast pointer at twice the speed of the slow pointer
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data

# Test the program
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

center_element = find_center_element(head)

print("Center Element:", center_element)
