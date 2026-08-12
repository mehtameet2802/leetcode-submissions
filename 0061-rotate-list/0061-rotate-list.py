# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        n = 0
        cur = head

        while cur:
            n += 1
            cur = cur.next
        
        k = k % n

        if k == 0:
            return head
        
        k = n - k

        prev = None
        temp = head
        while k > 0:
            prev = temp
            temp = temp.next
            k -= 1
        
        end = prev
        head2 = end.next
        end.next = None

        while temp:
            prev = temp
            temp = temp.next

        prev.next = head

        return head2