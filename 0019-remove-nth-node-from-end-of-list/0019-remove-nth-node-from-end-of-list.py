# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 0
        temp = head

        while temp:
            temp = temp.next
            cnt += 1
        
        n = cnt - n

        if n == 0:
            head = head.next
            return head

        temp = head
        while n>0:
            prev = temp
            temp = temp.next
            n -= 1 
        
        prev.next = temp.next
        return head