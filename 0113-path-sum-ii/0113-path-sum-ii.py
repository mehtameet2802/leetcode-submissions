# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        '''
        Pattern: Root-to-Leaf Path State + Backtracking

        Time:  O(n + L) precise
            O(n) traversal

        Space: O(h) auxiliary

        Optimal: Yes
        '''
        ans = []

        path = []

        def helper(root, cur):

            if not root:
                return

            cur = cur + root.val
            
            path.append(root.val)

            if not root.left and not root.right and cur == targetSum:
                ans.append(path.copy())
                path.pop()
                return
            
            if root.left:
                helper(root.left, cur)

            if root.right:
                helper(root.right, cur)

            path.pop()
        
        helper(root, 0)
        return ans
