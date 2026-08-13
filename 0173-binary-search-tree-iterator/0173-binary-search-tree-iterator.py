# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.arr = []
        self.idx = 0

        def helper(node):
            if not node:
                return
            
            helper(node.left)
            self.arr.append(node.val)
            helper(node.right)

        helper(self.root)

    def next(self) -> int:
        ele = self.arr[self.idx]
        self.idx += 1
        return ele
        

    def hasNext(self) -> bool:
        if self.idx < len(self.arr):
            return True
        
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()