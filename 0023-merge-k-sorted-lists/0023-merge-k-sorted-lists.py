# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(a,b):
            dummy = ListNode()
            temp = dummy

            while a and b:
                if a.val <= b.val:
                    temp.next = a
                    a = a.next
                else:
                    temp.next = b
                    b = b.next
                temp = temp.next
            
            if a:
                temp.next = a
            
            if b:
                temp.next = b
            
            return dummy.next


        if not lists:
            return None
        
        if len(lists) < 1:
            return lists
        
        a = lists[0]

        for i in range(1,len(lists)):
            b = lists[i]
            a = merge(a,b)
        
        return a