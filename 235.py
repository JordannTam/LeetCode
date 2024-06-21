# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = [-1]
        if root == None:
            return 0
        def search(node):
            if node == None:
                return False
            l = search(node.left)
            r = search(node.right)
            if (l and r) or (node.val == p.val and (l or r)) or (node.val == q.val and (l or r)) and res[0] == -1:
                res[0] = node.val
                return True
            if node.val == p.val or node.val == q.val:
                return True
            return l or r
        search(root)
        return res[0]
        