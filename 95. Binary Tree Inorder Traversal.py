class TreeNode:
    def __init__(self, val, left=0, right=0, next=None):
        self.val = val
        self.left = left
        self.right = right
        
def binary_inorder(root):
    result = []
    
    def helper(node):
        if node: #Check if node is present
            helper(node.left) #traverse left node as long as left node exists
            result.append(node.val) #append the node val
            helper(node.right) #traverse the right node, check first if left node exists for that right node
            
    helper(root)
    
    return result

# Example usage
root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(binary_inorder(root))  # Output: [1, 3, 2]
            