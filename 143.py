# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = 0
        r = 0
        stack = []

        curr = head
        while(curr != None):
            r += 1
            stack.append(curr)
            curr = curr.next
        curr = head        
        while(l <= r):
            rNode = stack.pop()
            r -= 1
            rNode.next = curr.next
            curr.next = rNode
            curr = curr.next.next
            l += 1
        curr.next = None
