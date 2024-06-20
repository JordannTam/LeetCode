# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        curr1 = list1
        curr2 = list2
        curr = None
        if curr1.val <= curr2.val:
            curr = curr1
            curr1 = curr1.next
        else:
            curr = curr2
            curr2 = curr2.next
        head = curr

        while(curr1 != None and curr2 != None):
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr = curr.next
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr = curr.next
                curr2 = curr2.next

        if curr1 == None:
            curr.next = curr2
        else:
            curr.next = curr1
        return head