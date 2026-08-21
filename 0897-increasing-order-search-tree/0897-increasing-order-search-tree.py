# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = root

        ans = None
        prev = None
        
        cur = root
        while cur:

            if cur.left is None:
                
                if prev:
                    prev.right = cur
                else:
                    ans = cur
                
                cur.left = None
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

                    if prev:
                        prev.right = cur
                    else:
                        ans = cur
                    
                    cur.left = None
                    prev = cur
                    cur = cur.right

        return ans
