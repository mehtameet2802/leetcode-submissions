# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
        
        ans = []

        def helper(root):
            nonlocal ans
            
            if not root:
                return

            helper(root.left)
            helper(root.right)
            ans.append(root.val)

        helper(root)
        return ans