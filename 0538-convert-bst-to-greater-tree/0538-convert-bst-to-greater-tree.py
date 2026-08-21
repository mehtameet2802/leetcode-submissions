# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curSum = 0

        cur = root

        while cur:

            if cur.right is None:
                curSum += cur.val
                cur.val = curSum
                cur = cur.left
            
            else:

                pre = cur.right

                while pre.left and pre.left != cur:
                    pre = pre.left
                
                if pre.left is None:
                    pre.left = cur
                    cur = cur.right
                
                else:
                    pre.left = None
                    curSum += cur.val
                    cur.val = curSum
                    cur = cur.left

        return root