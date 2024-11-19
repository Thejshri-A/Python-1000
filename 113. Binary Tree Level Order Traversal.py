# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 19:47:17 2024

@author: tejashri
"""

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def OrderLevel(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

# Example usage:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(OrderLevel(root))  # Output: [[3], [9, 20], [15, 7]]