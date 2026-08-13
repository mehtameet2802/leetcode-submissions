# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        '''
        Pattern:
        - Binary Tree
        - BFS
        - Queue
        - Level-order traversal

        TC - O(N)
        SC - O(W)
        Worst-case SC - O(N)
        '''
        
        if not root:
            return 0
        
        queue = deque([])
        depth = 0
        queue.append(root)

        while queue:
            length = len(queue)

            for _ in range(length):

                ele = queue.popleft()

                if not ele.left and not ele.right:
                    return depth + 1

                if ele.left:
                    queue.append(ele.left)

                if ele.right:
                    queue.append(ele.right)
            
            depth += 1
        
        return depth
        