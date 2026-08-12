# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        required = {}
        i = 0
        n = 0

        cur = head

        while cur:
            n += 1
            cur = cur.next
            
        ans = 0
        limit = (n // 2) - 1

        while head:
            if 0 <= i <= limit and 0 <= (n-i-1) < n :
                required[n-i-1] = head.val
            
            if i in required:
                ans = max(ans,head.val+required[i])
            
            i += 1
            head = head.next
        
        
        return ans
