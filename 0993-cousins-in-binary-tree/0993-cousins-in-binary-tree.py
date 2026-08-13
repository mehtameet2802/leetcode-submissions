# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([])
        queue.append(root)
        depth = 0

        d1 = p1 = d2 = p2 = None

        while queue:
            length = len(queue)

            for _ in range(length):
                ele = queue.popleft()

                if ele.left:
                    queue.append(ele.left)
                    if ele.left.val == x:
                        d1 = depth
                        p1 = ele
                    
                    if ele.left.val == y:
                        d2 = depth
                        p2 = ele
                
                if ele.right:
                    queue.append(ele.right)

                    if ele.right.val == x:
                        d1 = depth
                        p1 = ele
                    
                    if ele.right.val == y:
                        d2 = depth
                        p2 = ele
            
            depth += 1

            if d1 and d2:
                if d1 == d2 and p1 != p2:
                    return True
                return False

        return False