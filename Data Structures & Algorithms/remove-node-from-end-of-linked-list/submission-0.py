# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = ListNode()
        sentinel.next = head

        fast = head
        slow = sentinel

        for i in range(n):
            fast = fast.next
        

        while fast:
            slow = slow.next
            fast = fast.next

        del_node = slow.next
        slow.next = del_node.next

        return sentinel.next