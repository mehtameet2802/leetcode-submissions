# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        dummy = ListNode()
        dummy.next = head

        prev = dummy
        while head:
            cnt += 1

            i = 0
            temp = head
            while temp and i < cnt:
                temp = temp.next
                i += 1
            
            if i % 2==0:
                i = 0
                before = prev
                new_tail = prev.next
                while head and i < cnt:
                    temp = head.next
                    head.next = prev
                    prev = head
                    head = temp
                    i+=1
                before.next.next = head
                before.next = prev
                prev = new_tail
            else:
                i = 0
                while head and i<cnt:
                    prev = head
                    head = head.next
                    i += 1
        
        return dummy.next


            
