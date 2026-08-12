# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        temp = dummy

        while l1 and l2:
            cur = l1.val + l2.val + carry
            temp.next = ListNode(cur % 10)
            carry = cur // 10
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            cur = l1.val + carry
            temp.next = ListNode(cur % 10)
            carry = cur // 10
            temp = temp.next
            l1 = l1.next

        while l2:
            cur = l2.val + carry
            temp.next = ListNode(cur % 10)
            carry = cur // 10
            temp = temp.next
            l2 = l2.next

        if carry:
            temp.next = ListNode(carry)
        
        return dummy.next