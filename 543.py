# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def depth(node, h):
            if not node:
                return h
            else:
                left = depth(node.left, h + 1)
                right = depth(node.right, h + 1)
                return max(left, right)
            
        def inner(node):
            nonlocal result
            if not result:
                return
            total = depth(node.left, 0) + depth(node.right, 0)
            if total > result:
                result = total
            inner(node.left)
            inner(node.right)

        inner(root)
        return result

        
if __name__ == "__main__":
    s = Solution()
    print(Solution.diameterOfBinaryTree(s, [1,2,3,4,5]))
