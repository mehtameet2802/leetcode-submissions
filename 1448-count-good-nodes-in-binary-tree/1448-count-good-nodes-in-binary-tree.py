# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        TC = O(n)
        SC = O(h)
        '''

        def helper(node, maxVal):
            if not node:
                return 0
            
            count = 0

            if node.val >= maxVal:
                count += 1
            
            maxVal = max(maxVal, node.val)

            count += helper(node.left, maxVal)
            count += helper(node.right, maxVal)

            return count
        
        return helper(root, root.val)