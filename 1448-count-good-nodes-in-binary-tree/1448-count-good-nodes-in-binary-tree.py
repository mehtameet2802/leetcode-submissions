# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        cnt = 0

        def helper(node, maxVal):
            nonlocal cnt

            if not node:
                return
            
            if node.val >= maxVal:
                cnt += 1
            
            maxVal = max(maxVal, node.val)

            helper(node.left, maxVal)
            helper(node.right, maxVal)
        
        helper(root, root.val)
        return cnt