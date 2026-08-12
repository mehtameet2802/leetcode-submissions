# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        dummy.next = head

        right = right - left

        while left > 1:
            prev = head
            head = head.next
            left -= 1
        
        before = prev

        prev = None
        while right >= 0:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
            right -= 1
        
        before.next.next = head
        before.next = prev

        return dummy.next


