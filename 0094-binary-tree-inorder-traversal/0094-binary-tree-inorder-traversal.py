# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        '''
        Pattern:
        - Binary Tree
        - DFS
        - Recursion
        - Inorder Traversal

        TC - O(N)
        SC - O(H)

        H = tree height
        Balanced → O(log N)
        Skewed → O(N)
        '''
        
        ans = []

        def helper(root):
            nonlocal ans

            if not root:
                return
            
            helper(root.left)
            ans.append(root.val)
            helper(root.right)

            return

        helper(root)
        
        return ans