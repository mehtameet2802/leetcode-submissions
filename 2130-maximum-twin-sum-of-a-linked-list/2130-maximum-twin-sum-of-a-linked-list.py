# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # required = {}
        # i = 0
        # n = 0

        # cur = head

        # while cur:
        #     n += 1
        #     cur = cur.next
            
        # ans = 0
        # limit = (n // 2) - 1

        # while head:
        #     if 0 <= i <= limit and 0 <= (n-i-1) < n :
        #         required[n-i-1] = head.val
            
        #     if i in required:
        #         ans = max(ans,head.val+required[i])
            
        #     i += 1
        #     head = head.next
        
        
        # return ans

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None
        prev = None

        while head2:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp
        
        head2 = prev

        ans = 0

        while head and head2:
            ans = max(ans, head.val+head2.val)
            head = head.next
            head2 = head2.next
        
        return ans

