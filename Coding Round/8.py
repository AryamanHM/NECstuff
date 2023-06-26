class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root, k):
    stack = []
    count = 0
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        count += 1

        if count == k:
            return current.val

        current = current.right

    return None


# Test the function
# Create a binary search tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

k = 3

# Find the kth smallest element
kth_element = kth_smallest(root, k)

# Display the kth smallest element
if kth_element:
    print("The", k, "smallest element is:", kth_element)
else:
    print("The tree does not contain", k, "elements.")
