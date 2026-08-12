# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode()
        prev = dummy
        dummy.next = head
        
        while head:
            cnt = 0
            while head and prev.next.val == head.val:
                head = head.next
                cnt += 1
            
            if cnt > 1:
                prev.next = head
            else:
                prev = prev.next

        return dummy.next
            
