# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prefixSum = 0 
        # prefixSumMap = {}

        # dummy = ListNode()
        # dummy.next = head

        # prefixSumMap[0] = dummy

        # while head:
        #     prefixSum += head.val

        #     if prefixSum in prefixSumMap:
        #         prefixSumMap[prefixSum].next = head.next
        #         head = prefixSumMap[prefixSum]
        #     else:
        #         prefixSumMap[prefixSum] = head
            
        #     head = head.next
    

        # return dummy.next


        '''
        Pattern:
        - Prefix Sum
        - Hash Map
        - Linked List
        - Dummy Node

        TC - O(N)
        SC - O(N)
        '''

        prefixSum = 0 
        prefixSumMap = {}

        dummy = ListNode(0)
        dummy.next = head

        prefixSumMap[0] = dummy

        while head:
            prefixSum += head.val
            prefixSumMap[prefixSum] = head
            head = head.next

        head = dummy
        prefixSum = 0

        while head:
            prefixSum += head.val
            head.next = prefixSumMap[prefixSum].next
            head = head.next
    
        return dummy.next