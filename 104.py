# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(node, h):
            if not node:
                return h
            else:
                left = depth(node.left, h + 1)
                right = depth(node.right, h + 1)
                return max(left, right)
        return depth(root, 0)
