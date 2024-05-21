# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1
        
        lh = depth(root.left)
        rh = depth(root.right)

        if (lh - rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True

        return False
        


        
        
