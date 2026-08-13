# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # def helper(root1, root2):
        #     if not root1 and not root2:
        #         return None
            
        #     if not root1:
        #         new_node = TreeNode(root2.val)
        #         new_node.left = helper(None, root2.left)
        #         new_node.right = helper(None, root2.right)
        #         return new_node
            
        #     if not root2:
        #         new_node = TreeNode(root1.val)
        #         new_node.left = helper(root1.left, None)
        #         new_node.right = helper(root1.right, None)
        #         return new_node


        #     mergeSum = root1.val + root2.val

        #     new_node = TreeNode(mergeSum)

        #     new_node.left = helper(root1.left, root2.left)
        #     new_node.right = helper(root1.right, root2.right)
        
        #     return new_node

        # return helper(root1, root2)


        def helper(root1, root2):
            if not root1 and not root2:
                return None
            
            mergeSum = 0
            if root1:
                mergeSum += root1.val

            if root2:
                mergeSum += root2.val
            
            new_node = TreeNode(mergeSum)

            if not root1:
                left = helper(None, root2.left)
                right = helper(None, root2.right)
            elif not root2:
                left = helper(root1.left, None)
                right = helper(root1.right, None)
            else:
                left = helper(root1.left, root2.left)
                right = helper(root1.right, root2.right)

            new_node.left = left
            new_node.right = right
        
            return new_node

        return helper(root1, root2)


