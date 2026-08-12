# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode()
        prev = dummy
        dummy.next = list1
        b = b - a

        while a>0:
            prev = list1
            list1 = list1.next
            a -= 1
        
        prev.next = list2
        last = None

        while list2:
            last = list2
            list2 = list2.next

        prev = None
        while b > 0:
            prev = list1
            list1 = list1.next
            b -= 1
        
        last.next = list1.next

        return dummy.next