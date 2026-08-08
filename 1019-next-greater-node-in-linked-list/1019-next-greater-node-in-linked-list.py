# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        values = []

        while head:
            values.append(head.val)
            head = head.next

        for i, num in enumerate(values):
            while stack and values[stack[-1]] < num:
                j = stack.pop()
                values[j] = num
        
            stack.append(i)
        
        while stack:
            values[stack.pop()] = 0

        return values