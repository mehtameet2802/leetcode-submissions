# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = None
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            first.next = second.next
            second.next = first
            prev.next = second
            prev = first
            head = head.next
        
        return dummy.next

