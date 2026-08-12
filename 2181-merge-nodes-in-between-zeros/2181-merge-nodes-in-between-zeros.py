# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        temp1 = ans

        while head:
            if head.val == 0:
                cur = 0
                head = head.next
                while head and head.val != 0:
                    cur += head.val
                    head = head.next
                if cur > 0:
                    temp1.next = ListNode(cur)
                    temp1 = temp1.next
            else:
                head = head.next
        
        return ans.next