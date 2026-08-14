# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        '''
        Pattern: Root-to-Leaf Path State + Backtracking

        Time:  O(n) precise

        Space: O(h) auxiliary

        Optimal: Yes
        '''
        ans = 0

        def helper(root, cur):
            nonlocal ans

            if not root:
                return

            cur = cur * 10 + root.val

            if not root.left and not root.right:
                ans += cur
                return
            
            if root.left:
                helper(root.left, cur)

            if root.right:
                helper(root.right, cur)
        
        helper(root, 0)
        return ans
