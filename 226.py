# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        l = self.left
        self.left = self.invertTree(self.right)
        self.right = self.invertTree(l)
        return root




if __name__ == "__main__":
    s = Solution()
    print(Solution.invertTree(s, [4,2,7,1,3,6,9]))
