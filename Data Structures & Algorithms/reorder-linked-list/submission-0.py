# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow
        nxt = slow.next

        while nxt:
            nxtnxt = nxt.next
            nxt.next = cur
            cur = nxt
            nxt = nxtnxt
        
        left = head.next
        right = cur
        cur = head

        flag = True

        while True:
            if cur == slow:
                cur.next = None
                break
            if flag:
                cur.next = right
                right = right.next
                flag = False
            else:
                cur.next = left
                left = left.next
                flag = True
            cur = cur.next
            