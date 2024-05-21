    
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
        def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return head
            curr = head
            result = ListNode(val=curr.val)

            while(curr.next != None):
                curr = curr.next
                ListNode(val=curr.val, next=result)
            return result

        if not head:
            return
        count = 0
        curr = head
        while curr != None:
            count += 1
            curr = curr.next
        
        curr = head
        count = count // 2
        while count == 0:
            curr = curr.next
            count -= 1

        left = head
        right = reverseList(curr)

        node2 = ListNode(val=right.val)
        node1 = ListNode(val=left.val, next=node2)
        left=left.next
        right=right.next
        newHead = node1
        tail = node2

        while right != None:
            node2 = ListNode(val=right.val)
            node1 = ListNode(val=left.val, next=node2)
            tail.next = node1
            tail = node2
        
        head = newHead


        

        # curr = head
        # countN = count // 2
        # tail = None
        # newHead = curr

        # if count >= 2:
        #     node2 = ListNode(val=stack.pop().val)
        #     node1 = ListNode(val=curr.val, next=node2)
        #     countN - 1
        #     curr = curr.next
        #     tail = node2
        #     head = node1
        # else:
        #     return


        # while countN == 0 :
        #     node2 = ListNode(val=stack.pop().val)
        #     node1 = ListNode(val=curr.val, next=node2)
        #     tail.next = node1
        #     tail = node2
        #     curr = curr.next
        #     countN -= 1

        # head = newHead


