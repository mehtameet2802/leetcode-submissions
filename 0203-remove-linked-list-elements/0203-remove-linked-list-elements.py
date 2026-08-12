# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # TC - O(N)
        # SC - O(1)

        prev = None
        temp = head

        while temp:
            if temp.val == val:
                if not prev:
                    head = head.next
                elif not temp.next:
                    prev.next = None
                else:
                    prev.next = temp.next
            else:
                prev = temp
            temp = temp.next
        return head