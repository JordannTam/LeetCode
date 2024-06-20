# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepth(root):
            if root == None:
                return (0, 0)
            l = maxDepth(root.left)
            r = maxDepth(root.right)
            
            return (max(l[0], r[0]) + 1, max(max(l[0] + r[0], l[1]), r[1]))
        l, lmax = maxDepth(root.left)
        r, rmax = maxDepth(root.right)
        res = max(max(lmax, rmax), l + r)
        return res


        

        
if __name__ == "__main__":
    s = Solution()
    print(Solution.diameterOfBinaryTree(s, [1,2,3,4,5]))
