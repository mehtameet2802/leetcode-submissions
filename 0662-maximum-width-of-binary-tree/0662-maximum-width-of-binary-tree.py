# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Definition for a binary tree node.

        '''
        TC - O(N)
        SC - O(W)
        '''
        ans = -float('inf')

        if not root:
            return 0

        queue = deque([])
        queue.append((root,0))

        while queue:

            length = len(queue)

            for i in range(length):
                ele,d = queue.popleft()

                if i == 0:
                    s = d
                
                if i == length - 1:
                    e = d

                if ele.left:
                    queue.append((ele.left, 2*d+1))
                
                if ele.right:
                    queue.append((ele.right, 2*d+2))
            
            ans = max(ans, e - s + 1)

        return ans