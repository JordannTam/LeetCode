
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None:
            return None
        count = 0
        curr = l1

        while(curr):
            count += 1
            curr = curr.next
        
        
        prev = ListNode(0)
        curr = None
        head = prev
        while(count > 0):
            curr = ListNode(0)
            prev.next = curr
            prev = curr
            curr = None
            count -= 1

        
        # def getNext(n1, n2):
        #     if n1 == None:
        #         return 0
        #     getNext(n1.next, n2.next)

        #     return n1 + n2
