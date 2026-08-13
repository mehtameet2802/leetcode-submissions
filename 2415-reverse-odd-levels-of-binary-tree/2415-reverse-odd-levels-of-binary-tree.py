# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Definition for a binary tree node.

        '''
        TC - O(N)
        SC - O(W)
        '''

        if not root:
            return ans

        queue = deque([])
        queue.append(root)
        level = 0

        while queue:

            length = len(queue)

            nums = [num.val for num in queue]
            for i in range(length):
                ele = queue.popleft()

                if level % 2 == 1:
                    ele.val = nums[-1 - i] 

                if ele.left:
                    queue.append(ele.left)
                
                if ele.right:
                    queue.append(ele.right)
            
            level += 1

        return root