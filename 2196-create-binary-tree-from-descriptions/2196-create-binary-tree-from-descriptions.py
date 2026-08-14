# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tree_map = {}
        children = set()

        for nodeVal, childVal, left in descriptions:

            if childVal in tree_map:
                child = tree_map[childVal]
            else:
                child = TreeNode(childVal)

            if nodeVal in tree_map:
                node = tree_map[nodeVal]
            else:
                node = TreeNode(nodeVal)

            if left == 0:
                node.right = child
            else:
                node.left = child
            
            tree_map[nodeVal] = node
            tree_map[childVal] = child 
            children.add(childVal)

        for par, child in tree_map.items():
            if par in children:
                continue
            
            return tree_map[par]

        return None