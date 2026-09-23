# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        
        def remove(node, key):
            if not node:
                return None

            if node.val == key:
                if not node.left and not node.right:
                    return None

                if node.right:
                    suc = node.right

                    while suc and suc.left:
                        suc = suc.left

                    node.val = suc.val
                    node.right = remove(node.right, suc.val)
                    
                else:
                    suc = node.left

                    while suc and suc.right:
                        suc = suc.right
                
                    node.val = suc.val
                    node.left = remove(node.left, suc.val)
            
            elif node.val > key:
                node.left =  remove(node.left, key)
            else:
                node.right = remove(node.right, key)

            return node

        return remove(root, key)