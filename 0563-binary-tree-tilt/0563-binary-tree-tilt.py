# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        ans = 0

        def helper(node):
            nonlocal ans

            if not node:
                return 0

            l_total = helper(node.left)
            r_total = helper(node.right)

            tilt = abs(l_total - r_total)
            cur_total = l_total + r_total + node.val
            ans += tilt

            return cur_total

        helper(root)
        return ans