# Implement the in-order traversal of a binary tree (both recursively and iteratively).

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def inorder_traversal_recursive(root):
    result = []

    def inorder(node):
        if node:
            inorder(node.left)          # Visit left subtree
            result.append(node.value)   # Visit current node
            inorder(node.right)         # Visit right subtree

    inorder(root)
    return result


def inorder_traversal_iterative(root):
    result, stack = [], []
    current = root

    while current or stack:
        # Reach the leftmost node of the current node
        while current:
            stack.append(current)
            current = current.left

        # Current must be None at this point
        current = stack.pop()           # Node to be visited
        result.append(current.value)    # Visit current node

        # Visit the right subtree
        current = current.right

    return result

# Example Tree:
#      1
#       \
#        2
#       /
#      3


# Creating the tree nodes
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Recursive In-order Traversal
print("Recursive In-order Traversal:")
print(inorder_traversal_recursive(root))  # Output: [1, 3, 2]

# Iterative In-order Traversal
print("Iterative In-order Traversal:")
print(inorder_traversal_iterative(root))  # Output: [1, 3, 2]
