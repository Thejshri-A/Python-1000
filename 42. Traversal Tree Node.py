class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val= val
        self.left=left
        self.right=right
    
def inorderTraversal(root):
    result=[]
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    inorder(root)
    return result

root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
print(inorderTraversal(root))
            