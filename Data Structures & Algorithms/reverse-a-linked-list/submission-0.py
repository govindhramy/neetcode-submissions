# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        cur = head
        nxt = head.next
        cur.next = None

        while nxt:
            nxtnxt = nxt.next
            nxt.next = cur
            cur = nxt
            nxt = nxtnxt
        
        return cur