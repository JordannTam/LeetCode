# Definition for a binary tree node.
import collections
from typing import List, Optional


# Definition for a binary tree node.
# LevelOrder(tree)

# Create an empty queue Q
# Enqueue the root node of the tree to Q
# Loop while Q is not empty
# Dequeue a node from Q and visit it
# Enqueue the left child of the dequeued node if it exists
# Enqueue the right child of the dequeued node if it exists

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = collections.deque()
        queue.append(root)
        res = []
        while(queue):
            qLen = len(queue)
            level = []
            for _ in range(qLen):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        return res
