# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def findTarget(top):
            if top.left == None and top.right == None:
                if top.val != p and top.val != q:
                    return False, False, None
                elif top.val == q:
                    return False, True, None
                elif top.val == p:
                    return True, False, None
            else:
                hasP, hasQ, T = False, False, None
                if top.left != None:
                    tempP, tempQ, tempT = findTarget(top.left)
                    hasP, hasQ, T = tempP|hasP, tempQ|hasQ, tempT
                if top.right != None:
                    tempP, tempQ, tempT = findTarget(top.right)
                    hasP, hasQ, T = tempP|hasP, tempQ|hasQ, tempT
                # Case 1 : left and right are not the targets
                if top.val != p or top.val != q:
                    if T == None and hasP and hasQ:
                        return hasP, hasQ, top.val
                    else:
                        return hasP, hasQ, T
                # Case 2 : left is the target, right is not.
                if top.val == p:
                    if hasQ:
                        return True, hasQ, top.val
                    else:
                        return True, hasQ, T
                # Case 3 : left is not the target, right is the target
                if top.val == q:
                    if hasP:
                        return hasP, True, top.val
                    else:
                        return hasP, True, T
        _, _, result = findTarget(root)
        return result


if __name__ == '__main__':
    S = Solution
    print(Solution.lowestCommonAncestor(S, [1,2,3], 2, 3))






