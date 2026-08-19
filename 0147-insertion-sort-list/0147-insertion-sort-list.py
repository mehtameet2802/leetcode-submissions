# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy

        length = 0

        while head:
            prev = dummy
            temp = dummy.next
            if not temp:
                prev = dummy
                prev.next = head
            else:
                while temp and temp.val <= head.val:
                    prev = temp
                    temp = temp.next
                prev.next = head
        

            head = head.next
            prev = prev.next
            prev.next = temp

        return dummy.next
            