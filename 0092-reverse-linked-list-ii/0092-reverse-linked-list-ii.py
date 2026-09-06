# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cnt = 1
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while cnt < left:
            cnt += 1
            prev = head
            head = head.next
            
        before = prev
        temp = head

        while cnt <= right:
            head = head.next
            temp.next = prev
            prev = temp
            temp = head
            cnt += 1
        

        before.next.next = head
        before.next = prev

        return dummy.next
