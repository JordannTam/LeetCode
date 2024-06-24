# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        res = [0]
        
        def dfs (node, maxNum):
            if node == None:
                return
            if node.val >= maxNum:
                res[0] += 1
            l = dfs(node.left, max(maxNum, node.val))
            r = dfs(node.right, max(maxNum, node.val))
            
        dfs(root, root.val)
        return res[0]
