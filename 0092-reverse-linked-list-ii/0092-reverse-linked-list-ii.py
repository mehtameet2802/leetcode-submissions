# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        What node must stay connected before the reversed section?
        What is the first node of the section before reversal? - before
        What node follows the reversed section? - prev
        What does each pointer represent?
        prev - previous
        before- before left
        temp - used temperary reversal
        Invariant during reversal: while head
        How do I reconnect both ends? - 
        Dangerous case: left = 1, we will add dummy node
        Complexity: O(n)
        '''

        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cnt = 1

        while cnt < left:
            prev = head
            head = head.next
            cnt += 1

        before = prev

        while cnt <= right:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
            temp = head
            cnt += 1
        
        before.next.next = head
        before.next = prev

        return dummy.next

