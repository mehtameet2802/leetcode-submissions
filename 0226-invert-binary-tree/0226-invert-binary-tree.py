# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Pattern:
        - Binary Tree
        - DFS
        - Recursion
        - In-place modification

        TC - O(N)
        SC - O(H)

        Balanced → O(log N)
        Worst case → O(N)

        Optimal → Yes
        '''

        def helper(root):
            if not root:
                return
            
            root.left, root.right = root.right, root.left

            helper(root.left)
            helper(root.right)

        helper(root)
        return root
