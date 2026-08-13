# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        '''
        TC - O(N)
        SC - O(H)
        '''

        prev = None
        ans = float('inf')

        def helper(node):
            nonlocal prev
            nonlocal ans

            if not node:
                return
            
            helper(node.left)

            if not prev:
                prev = node
            else:
                ans = min(ans, node.val - prev.val)
                prev = node

            helper(node.right)

        helper(root)            
            
        return ans
