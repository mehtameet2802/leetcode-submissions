# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(left, right):
            dummy = ListNode()
            temp = dummy
            while left and right:
                if left.val <= right.val:
                    temp.next = left
                    left = left.next
                else:
                    temp.next = right
                    right = right.next
                temp = temp.next

            if left:
                temp.next = left
            
            if right:
                temp.next = right
            
            return dummy.next


        def mergeSort(head):
            if not head or not head.next:
                return head

            slow = head
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            head2 = slow.next
            slow.next = None
            left = mergeSort(head)
            right = mergeSort(head2)

            return merge(left,right)

        return mergeSort(head)
