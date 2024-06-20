# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        def maxDepth(root):
            if root == None:
                return (0, True)
            l = maxDepth(root.left)
            r = maxDepth(root.right)
            res = False
            if l[0] + 1 == r[0] or r[0] + 1 == l[0] or r[0] == l[0]:
                res = True
            res = res and l[1] and r[1]
            return (max(l[0], r[0]) + 1, res)
        l = maxDepth(root.left)
        r = maxDepth(root.right)
        res = False
        if l[0] + 1 == r[0] or r[0] + 1 == l[0] or r[0] == l[0]:
            res = True
        return res and l[1] and r[1]
