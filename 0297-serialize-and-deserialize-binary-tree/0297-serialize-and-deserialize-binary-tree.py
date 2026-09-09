# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    '''
    Required output: - convert tree to serialized string, and then deserialize the string to get the tree
    What must serialization preserve? - the 
    How will a missing child be represented? - -1001 value
    What does deserialize consume at each step? 
    What does recursive helper return? - 
    Invariant:
    Pseudocode:
    Complexity: - O(n), SC - O(n) - for the arrat used
    Dangerous cases:
    '''

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        queue = deque()
        queue.append(root)
        serialized = [str(root.val)]

        while queue:
            
            length = len(queue)

            for _ in range(length):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    serialized.append(str(node.left.val))
                else:
                    serialized.append("#")
                
                if node.right:
                    queue.append(node.right)
                    serialized.append(str(node.right.val))
                else:
                    serialized.append("#")

        return ",".join(serialized)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        deserialized = data.split(",")
        if data == "":
            return None
        
        root = TreeNode(deserialized[0])
        queue = deque()
        queue.append(root)
        i = 0

        while queue:
            length = len(queue)

            for _ in range(length):
                node = queue.popleft()

                i+=1

                if deserialized[i] != "#":
                    left_node = TreeNode(int(deserialized[i]))
                    node.left = left_node
                    queue.append(left_node)
                else:
                    node.left = None
                    
                i+=1
                if deserialized[i] != "#":
                    right_node = TreeNode(int(deserialized[i]))
                    node.right = right_node
                    queue.append(right_node)
                else:
                    node.right = None
        
        return root

        

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))