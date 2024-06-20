from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        pointer = None
        while (curr.next != None):
            stack.append(curr)
            curr = curr.next
        pointer = curr
        while(stack):
            prevN = stack.pop()
            pointer.next = prevN
            pointer = pointer.next
        pointer.next = None
        return curr
