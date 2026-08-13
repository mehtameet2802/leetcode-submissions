# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''
        Pattern:
        - BST
        - Search
        - Recursion / Iteration

        Recursive:
        TC - O(H)
        SC - O(H)

        Iterative:
        TC - O(H)
        SC - O(1)  ← better

        Balanced → O(log N)
        Worst case → O(N)7
        '''
        
        while root:
            if not root:
                return None
            
            if root.val == val:
                return root
            
            if root.val < val:
                root = root.right
            else:
                root = root.left
        
            
