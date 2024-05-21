# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        left = self.levelOrder(root.left)
        right = self.levelOrder(root.right)

        nl = len(left)
        nr = len(right)
        
        arr = []
        n = min(nl,nr)
        for i in range(n):
            arr.append(left[i] + right[i])
        arr = arr + left[n:] + right[n:]

        return arr