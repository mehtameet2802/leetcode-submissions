# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        ans = []

        if not root:
            return ""

        def helper(node):
            if not node:
                return
            
            ans.append(str(node.val))
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return ",".join(ans)


    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None

        data = data.split(",")
        values = list(map(int,data))
        idx = 0

        def helper(low,high):
            nonlocal idx
            
            if idx >= len(values):
                return None 

            val = values[idx]

            if val < low or val > high:
                return None
            
            node = TreeNode(val)
            idx += 1

            node.left = helper(low, val)
            node.right = helper(val, high)

            return node
        
        return helper(-float('inf'),float('inf'))


        return None
        
            
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans