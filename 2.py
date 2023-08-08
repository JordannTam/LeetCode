# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        increment = 0
        head = ListNode()
        curr = head
        while curr1 != None and curr2 != None:
            total = curr2.val + curr1.val + increment
            increment = 0
            if total > 9:
                total = total - 10
                increment = 1
            curr.val = total
            curr1 = curr1.next
            curr2 = curr2.next
            if curr1 and curr2 != None:
                curr.next = ListNode()
                curr = curr.next
            total = 0

        return head


if __name__ == "__main__":
    Solution.addTwoNumbers()
