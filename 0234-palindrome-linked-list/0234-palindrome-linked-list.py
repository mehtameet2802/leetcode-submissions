# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # s1 = []

        # while head:
        #     s1.append(head.val)
        #     head = head.next
        
        # return s1 == s1[::-1]

        if not head or not head.next:
            return True

        fast = head
        slow = head

        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if fast:
            head2 = slow.next
            prev.next = None
        else:
            head2 = slow
            prev.next = None

        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        head = prev
        while head and head2:
            if head.val != head2.val:
                return False
            
            head = head.next
            head2 = head2.next
        
        if not head and not head2:
            return True
        
        return False