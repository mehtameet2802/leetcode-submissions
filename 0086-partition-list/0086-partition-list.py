# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # dummy = ListNode()
        # dummy.next = head

        # less = ListNode()
        # temp = less
        # prev = dummy

        # while head:
        #     if head.val < x:
        #         new_node = head

        #         prev.next = head.next
        #         head = head.next

        #         new_node.next = None
        #         temp.next = new_node
        #         temp = temp.next
        #     else:
        #         prev = head
        #         head = head.next
            
        # if less.next:
        #     temp.next = dummy.next
        #     return less.next
        
        # return dummy.next

        '''
        Pattern:
        - Linked List
        - Two Chains

        TC - O(N)
        SC - O(1)
        '''

        less = ListNode()
        greater = ListNode()

        less_ptr = less
        greater_ptr = greater

        while head:

            if head.val < x:
                less_ptr.next = head
                less_ptr = less_ptr.next

            else:
                greater_ptr.next = head
                greater_ptr = greater_ptr.next

            head = head.next

        # End the greater/equal list
        greater_ptr.next = None

        # Connect the two lists
        less_ptr.next = greater.next

        return less.next

