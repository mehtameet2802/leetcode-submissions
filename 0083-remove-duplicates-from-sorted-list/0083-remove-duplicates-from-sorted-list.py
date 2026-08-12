# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = head
        temp = head.next

        while temp:
            while prev and temp and temp.val == prev.val:
                temp = temp.next
            prev.next = temp
            prev = temp

            if temp:
                temp = temp.next
        
        return head
