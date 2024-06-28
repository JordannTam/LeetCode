# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root == None:
            return root.val
        res = [0]
        pos = [0]
        def findK (node):
            # left 
            if node == None:
                return
            findK(node.left)
            pos[0] += 1
            if pos[0] == k:
                res[0] = node.val
            findK(node.right)
            return
            
        findK(root)
        return res[0]