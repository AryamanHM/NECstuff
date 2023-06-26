class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def is_palindrome(head):
    # Check if the linked list is empty or has only one element
    if head is None or head.next is None:
        return True

    # Find the middle node using the slow-fast pointer technique
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    second_half = reverse_linked_list(slow.next)
    slow.next = None

    # Compare the first half with the reversed second half
    first_half = head
    while first_half and second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True


def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


# Test the program
# Create a palindrome linked list: 1 -> 2 -> 3 -> 2 -> 1
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

if is_palindrome(head):
    print("Palindrome Linked List")
else:
    print("Not a Palindrome Linked List")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        popped_value = self.head.data
        self.head = self.head.next
        return popped_value

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.head.data


# Test the stack implementation
stack = Stack()

# Push elements into the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Pop elements from the stack
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2

# Get the top element without popping
print(stack.peek())  # Output: 1
