class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
        curr = head
        result = ListNode(val=curr.val)

        while(curr.next != None):
            curr = curr.next
            ListNode(val=curr.val, next=result)
        
        return result