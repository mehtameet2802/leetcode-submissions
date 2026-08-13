# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # arr = []

        # while head:
        #     arr.append(head.val)
        #     head = head.next
        
        # def build(l,r):
        #     if l > r:
        #         return None
            
        #     mid = (l+r)//2

        #     node = TreeNode(arr[mid])
        #     node.left = build(l, mid-1)
        #     node.right = build(mid+1, r)

        #     return node
        
        # return build(0, len(arr)-1)


        def build(l, r):

            if l == r:
                return None

            slow = l
            fast = l

            while fast != r and fast.next!=r:
                slow = slow.next
                fast = fast.next.next
            
            node = TreeNode(slow.val)
            node.left = build(l, slow)
            node.right = build(slow.next, r)
        
            return node
        
        return build(head, None)
