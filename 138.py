# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head
        curr = head
        while(curr):
            newNode = Node(curr.val, next=curr.next)
            curr.next = newNode
            curr = newNode.next
        curr = head
        while(curr):
            newNode = curr.next
            if curr.random:
                newNode.random = curr.random.next
            else:
                newNode.random = None
            curr = curr.next.next
        
        newHead = head.next
        newCurr = head.next
        while(newCurr):
            newCurr.next = newCurr.next.next
            newCurr = newCurr.next
        
        return newHead
