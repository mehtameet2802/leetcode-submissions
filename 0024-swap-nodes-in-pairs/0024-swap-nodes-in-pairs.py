# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        first = head

        if head:
            second = head.next
        else:
            second = None

        while second:
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
            
            first = first.next

            if first:
                second = first.next
            else:
                second = None
        
        return dummy.next
