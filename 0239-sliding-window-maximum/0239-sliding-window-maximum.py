class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        queue = deque()
        ans = []

        for i, num in enumerate(nums):
            while queue and nums[queue[-1]] < num:
                queue.pop()
            
            while queue and queue[0] <= (i-k):
                queue.popleft()
            
            queue.append(i)

            if i>=k-1:
                ans.append(nums[queue[0]])
        
        return ans