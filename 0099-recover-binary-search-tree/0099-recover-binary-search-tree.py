# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        cur = root
        prev = None
        first = None
        second = None

        while cur:

            if cur.left is None:

                if prev and prev.val > cur.val:
                    
                    if first is None:
                        first = prev

                    second = cur 

                prev = cur
                cur = cur.right
            
            else:

                pre = cur.left

                while pre.right and pre.right != cur:
                    pre = pre.right
                
                if pre.right is None:
                    pre.right = cur
                    cur = cur.left
                
                else:
                    pre.right = None

                    if prev and prev.val > cur.val:
                        if first is None:
                            first = prev
                        
                        second = cur
                    prev = cur
                    cur = cur.right
        
        first.val, second.val = second.val, first.val