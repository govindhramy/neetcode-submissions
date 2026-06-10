# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2

        if h2 is None:
            return h1
        if h1 is None:
            return h2
        
        if h1.val <= h2.val:
            head = h1
            h1 = h1.next
        else:
            head = h2
            h2 = h2.next
        
        cur = head

        while h1 and h2:
            if h2.val < h1.val:
                cur.next = h2
                cur = h2
                h2 = h2.next
            else:
                cur.next = h1
                cur = h1
                h1 = h1.next
        
        if h1:
            cur.next = h1
        else:
            cur.next = h2
        
        return head
            

