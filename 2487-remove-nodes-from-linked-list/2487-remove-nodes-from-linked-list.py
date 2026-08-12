# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        head = prev
        cur = head

        while cur and cur.next:

            if cur.next.val < cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        return prev

