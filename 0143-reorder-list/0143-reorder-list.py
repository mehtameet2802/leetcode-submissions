# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        '''
        Pattern - Divide in 2 parts and merge

        TC - O(N)
        SC - O(1) 
        '''

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow
        slow = None

        prev = None
        while head2:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp
        
        head2 = prev

        dummy = head

        while head and head2:
            temp = head.next
            head.next = head2
            head = temp

            temp = head2.next
            head2.next = head
            head2 = temp
        
        return dummy
