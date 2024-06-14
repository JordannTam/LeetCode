from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return head
        if (head.next == None):
            return head
        oddIndicator = True
        oddListHead = head
        evenListHead = head.next
        currNode = head.next.next
        oddListCurr = oddListHead
        evenListCurr = evenListHead
        
        while(currNode != None):
            if (oddIndicator):
                oddListCurr.next = currNode
                oddListCurr = oddListCurr.next
            else:
                evenListCurr.next = currNode
                evenListCurr = evenListCurr.next
            oddIndicator = not oddIndicator
            currNode = currNode.next
        evenListCurr.next = None
        oddListCurr.next = evenListHead
        return oddListHead