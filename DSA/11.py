class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def left_view(root):
    if not root:
        return

    # Create an empty queue for level-order traversal
    queue = []
    # Enqueue the root node
    queue.append(root)

    while queue:
        # Get the number of nodes at the current level
        level_nodes = len(queue)

        for i in range(level_nodes):
            # Dequeue the front node
            node = queue.pop(0)

            # Print the first node of each level (leftmost node)
            if i == 0:
                print(node.data, end=" ")

            # Enqueue the left child if it exists
            if node.left:
                queue.append(node.left)
            # Enqueue the right child if it exists
            if node.right:
                queue.append(node.right)

# Test the program
# Create a binary search tree
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
root.right.right.right = Node(8)

print("Left View of Binary Search Tree:")
left_view(root)
