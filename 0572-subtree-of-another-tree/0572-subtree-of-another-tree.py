# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        Pattern:
        - Binary Tree
        - DFS
        - Subtree Matching
        - Recursion

        TC - O(N × M)
        SC - O(H₁ + H₂)
        '''
        
        def check(root1, subRoot):
            if not root1 and not subRoot:
                return True
            
            if not root1 or not subRoot:
                return False

            if root1.val != subRoot.val:
                return False
            
            return check(root1.left, subRoot.left) and check(root1.right, subRoot.right)

        def helper(root):
            if not root:
                return False

            if root.val == subRoot.val:
                if check(root, subRoot):
                    return True

            return helper(root.left) or helper(root.right)

        return helper(root)