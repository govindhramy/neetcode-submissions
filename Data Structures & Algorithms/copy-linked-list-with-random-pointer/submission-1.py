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
        if not head:
            return None

        cur = head

        while cur:
            cpy = Node(cur.val)

            nxt = cur.next
            cur.next = cpy
            cpy.next = nxt

            cur = nxt
        
        prev = head
        cur = head.next

        while cur:
            if prev.random:
                cur.random = prev.random.next 
            prev = cur.next
            cur = prev.next if prev else None
        
        copy_head = head.next
        prev = head
        cur = head.next

        while cur:
            prev.next = cur.next
            cur.next = prev.next.next if prev.next else None
            prev = prev.next
            cur = cur.next
        
        return copy_head
