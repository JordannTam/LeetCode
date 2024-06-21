# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIdentical(r, s):
            if r == None and s == None:
                return True
            if r.val == s.val:
                return isIdentical(r.left, s.left) and isIdentical(r.right, s.right)
            
            return isIdentical(r.left, s) or isIdentical(r.right, s)
        