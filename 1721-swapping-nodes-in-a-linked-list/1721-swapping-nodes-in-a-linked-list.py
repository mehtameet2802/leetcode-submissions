# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = head

        for _ in range(k-1):
            fast = fast.next
        
        first = fast

        slow = head

        while fast.next:
            fast = fast.next
            slow = slow.next
        

        slow.val, first.val = first.val, slow.val

        return head