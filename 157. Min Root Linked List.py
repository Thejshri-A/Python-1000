class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val =val
        self.left = left
        self.right = right
        
def min_depth(root):
    if not root:
        return 0
    
    if not root.left or not root.right:
        return 1+ max(min_depth(root.left), min_depth(root.right))
    return 1+min(min_depth(root.left), min_depth(root.right))


# Example usage:
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(min_depth(root))  # Output: 2