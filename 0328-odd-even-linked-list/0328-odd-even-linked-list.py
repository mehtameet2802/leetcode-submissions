# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()

        odd_temp = odd
        even_temp = even
        cnt = 1

        while head:
            if cnt % 2 == 0:
                even_temp.next = head
                even_temp = even_temp.next
            else:
                odd_temp.next = head
                odd_temp = odd_temp.next
            
            head = head.next
            cnt += 1
        
        odd = odd.next
        even = even.next
        even_temp.next = None
        odd_temp.next = even

        return odd

