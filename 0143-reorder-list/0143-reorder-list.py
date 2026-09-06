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
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        prev = None
        temp = head2
        while head2:
            head2 = head2.next
            temp.next = prev
            prev = temp
            temp = head2
        
        head2 = prev

        ans = ListNode()
        temp = ans

        while head or head2:
            if head:
                temp.next = head
                head = head.next
                temp = temp.next
            
            if head2:
                temp.next = head2
                head2 = head2.next
                temp = temp.next

        return ans.next
