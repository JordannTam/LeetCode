# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        curr = head
        count = 0
        while curr != None:
            count += 1
            curr = curr.next
        if count < n:
            return head
        

        curr = head
        prev = None

        m = count - n
            
        if m == 0:
            return head.next
        
        count = 0
        
        
        while count != m and curr != None:
            prev = curr
            curr = curr.next
            count += 1
        if prev is None:
            return None
        else:
            prev.next = curr.next



        return head