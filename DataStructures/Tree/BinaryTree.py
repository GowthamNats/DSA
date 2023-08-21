class Node:
    # Implementation
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Preorder Traversal
    def traversePreOrder(self):
        print(self.val, end=" ")
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Inorder Traversal
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=" ")
        if self.right:
            self.right.traverseInOrder()

    # Postorder Traversal
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()   
        print(self.val, end=" ")    

# Check for full binary tree
def isFullTree(root):
    if root is None:
        return True
    
    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return isFullTree(root.left) and isFullTree(root.right)
    
    return False

# Calculate depth of a binary tree for checking perfert bianry trees
def calculateDepth(root):
    d = 0
    while root is not None:
        d += 1
        root = root.left
    return d
    
# Check for perfect binary tree
def isPerfectTree(root, d, level=0):
    if root is None:
        return True
    
    if root.left is None and root.right is None:
        return (d == level + 1)

    if root.left is None or root.right is None:
        return False
    
    return isPerfectTree(root.left, d, level+1) and isPerfectTree(root.right, d, level+1)

# Count the number of nodes
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Check for complete binary tree
def isCompleteTree(root, index, numberNodes):
    if root is None:
        return True
    
    if index >= numberNodes:
        return False
    
    return isCompleteTree(root.left, index*2 + 1, numberNodes) and isCompleteTree(root.right, index*2 + 2, numberNodes)

# Implementation to check for tree balance
class Height:
    def __init__(self):
        self.height = 0

def isHeightBalanced(root, height):
    left_height = Height()
    right_height = Height()

    if root is None:
        return True
    
    l = isHeightBalanced(root.left, left_height)
    r = isHeightBalanced(root.right, right_height)

    height.height = max(left_height.height, right_height.height)

    if abs(left_height.height - right_height.height) <= 1:
        return l and r