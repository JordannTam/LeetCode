# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


## Attempt 1
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if root == None:
#             return True
#         if root.left == None and root.right == None:
#             return True
            
#         def dfs (node, parentNums):
#             if node == None:
#                 return True
#             lP = parentNums[:]
#             rP = parentNums[:]
#             lP.append((node.val, True))
#             rP.append((node.val, False))
#             l = dfs(node.left, lP)
#             r = dfs(node.right, rP)
#             if not all(map(lambda x: node.val < x[0] if x[1] else node.val > x[0] , parentNums)):
#                 return False
#             return l and r
#         l = dfs(root.left, [(root.val, True)])
#         r = dfs(root.right, [(root.val, False)])
#         return l and r

# Attempt 2

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        def isValid(node, left, right):
            if node == None:
                return True
            if node.val <= left or node.val >= right:
                return False
            
            return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)
        return isValid(root, float("-inf"), float("inf"))
