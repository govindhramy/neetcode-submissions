# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = l1
        j = l2

        sentinel = ListNode()
        prev = sentinel
        carryover = 0

        while i or j or carryover:
            s = (i.val if i else 0) + (j.val if j else 0) + carryover
            print(s)
            carryover = s//10
            node = ListNode(s%10)
            prev.next = node
            prev = node
            i = i.next if i else None
            j = j.next if j else None
        
        return sentinel.next
