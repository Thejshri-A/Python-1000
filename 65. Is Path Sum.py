class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def is_path_sum(root, targetSum):
    if not root:
        return False
    if not root.left and not root.right and root.val==targetSum:
        return True
    targetSum -= root.val
    return is_path_sum(root.left, targetSum) or is_path_sum(root.right, targetSum)
    

# Example
root = TreeNode(5)
root.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
root.right = TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))

targetSum = 22
print(is_path_sum(root, targetSum))