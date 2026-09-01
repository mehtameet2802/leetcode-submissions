# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        ans = 0
        def helper(node):
            nonlocal ans

            if not node:
                return
            
            helper(node.right)
            
            ans += node.val
            node.val = ans

            helper(node.left)

            return
        
        helper(root)
        return root



