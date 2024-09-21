class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right =right

def lowestCommonAncestor(root, p, q):
    if(p.val<root.val and q.val<root.val):
        root=root.left
    elif p.val>root.val and q.val>root.val:
        root=root.right
    else:
        return root

root = TreeNode(6, TreeNode(2), TreeNode(8))
p = TreeNode(2)
q = TreeNode(8)
print(lowestCommonAncestor(root, p, q).val)  # Output: 6

    