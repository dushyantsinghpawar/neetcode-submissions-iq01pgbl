"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head: return None
        
        l1 = head
        while l1:
            inter = Node(l1.val)
            inter.next = l1.next
            l1.next = inter
            l1 = inter.next

        newHead = head.next

        l1 = head
        while l1:
            inter = l1.next
            if l1.random:
                inter.random = l1.random.next
            l1 = l1.next.next

        l1 = head
        while l1:
            inter = l1.next
            l1.next = inter.next
            if inter.next:
                inter.next = inter.next.next
            l1 = l1.next

        return newHead
