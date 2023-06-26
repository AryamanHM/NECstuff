class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_sort_linked_list(head):
    # Base case: If the list is empty or has only one element, return the list
    if head is None or head.next is None:
        return head

    # Split the list into two halves
    mid = get_middle_node(head)
    left_half = head
    right_half = mid.next
    mid.next = None

    # Recursively sort the two halves
    sorted_left = merge_sort_linked_list(left_half)
    sorted_right = merge_sort_linked_list(right_half)

    # Merge the sorted halves
    sorted_list = merge(sorted_left, sorted_right)

    return sorted_list


def get_middle_node(head):
    if head is None:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge(left, right):
    # Create a dummy node as the new head of the merged list
    dummy = Node(0)
    current = dummy

    # Merge the two sorted lists
    while left and right:
        if left.data <= right.data:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next

    # Append any remaining nodes from the left or right list
    if left:
        current.next = left
    if right:
        current.next = right

    return dummy.next


def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()


# Test the program
# Create a linked list: 7 -> 2 -> 4 -> 1 -> 5
head = Node(7)
head.next = Node(2)
head.next.next = Node(4)
head.next.next.next = Node(1)
head.next.next.next.next = Node(5)

print("Original Linked List:")
print_linked_list(head)

# Sort the linked list
sorted_list = merge_sort_linked_list(head)

print("Sorted Linked List:")
print_linked_list(sorted_list)
