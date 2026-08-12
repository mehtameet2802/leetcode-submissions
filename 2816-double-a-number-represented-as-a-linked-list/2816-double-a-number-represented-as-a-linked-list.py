# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        carry = 0
        head = prev
        
        prev = None
        while head:

            value = carry + (head.val * 2) 
            head.val = value % 10
            carry = value // 10

            temp = head.next
            head.next = prev
            prev = head
            head = temp

        if carry > 0:
            new_node =  ListNode(carry)
            new_node.next = prev
            prev = new_node
        
        return prev
