# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Pattern:
        - Binary Tree
        - DFS
        - Recursion

        TC - O(N)
        SC - O(H)

        Balanced → O(log N)
        Worst case → O(N)
        '''
        
        def helper(root):
            if not root:
                return 0
            
            return max(helper(root.left), helper(root.right)) + 1
        
        return helper(root)