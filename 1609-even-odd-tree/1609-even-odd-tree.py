# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        '''
        TC - O(N)
        SC - O(W)
        '''

        level = 0

        if not root:
            return False

        queue = deque([])
        queue.append(root)

        while queue:

            length = len(queue)

            if level % 2 == 0:
                prev = -float('inf')
            else:
                prev = float('inf')

            for i in range(length):
                ele = queue.popleft()

                if level % 2 == 0:
                    if ele.val % 2 == 0 or ele.val <= prev:
                        return False
                else:
                    if ele.val % 2 == 1 or ele.val >= prev:
                        return False
                
                prev = ele.val

                if ele.left:
                    queue.append(ele.left)
                
                if ele.right:
                    queue.append(ele.right)
            
            level += 1

        return True