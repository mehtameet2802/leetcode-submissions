# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    '''
    What information must serialization preserve?
    How will null children be represented?
    What does the serialization queue contain?
    What does the deserialization queue contain?
    What does the token pointer represent?
    How many tokens does each processed parent consume?
    Serialization invariant:
    Deserialization invariant:
    Expected TC and SC:
    '''

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        serialized = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if not node:
                serialized.append("#")
            else:
                serialized.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        
        return ",".join(serialized)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        deserialized = data.split(",")

        idx = 0
        root = TreeNode(int(deserialized[idx]))
        queue = deque([root])

        while queue:
            node = queue.popleft()

            idx += 1
            if idx<len(deserialized):
                if deserialized[idx] == "#":
                    node.left = None
                else:
                    node.left = TreeNode(int(deserialized[idx]))
                    queue.append(node.left)

            idx += 1
            if idx<len(deserialized):
                if deserialized[idx] == "#":
                    node.right = None
                else:
                    node.right = TreeNode(int(deserialized[idx]))
                    queue.append(node.right)

        return root 



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))