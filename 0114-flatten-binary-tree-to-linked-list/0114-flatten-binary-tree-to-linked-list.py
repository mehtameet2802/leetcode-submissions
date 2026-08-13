# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        '''
        Pattern:
        - Binary Tree
        - DFS
        - Postorder-style processing
        - In-place modification

        TC - O(N)
        SC - O(H)
        '''

        def helper(root):
            if not root:
                return None

            left_tail = helper(root.left)
            right_tail = helper(root.right)

            if left_tail:
                left_tail.right = root.right
                root.right = root.left
                root.left = None
            
            if right_tail:
                return right_tail
            
            if left_tail:
                return left_tail
            
            return root
        
        return helper(root)
        