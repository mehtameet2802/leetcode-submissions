class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        queue = deque()
        n = len(nums)
        prefix_sum = [0] * (n+1)
        cur_sum = 0
        ans = float('inf')

        for i in range(n+1):
            prefix_sum[i] = cur_sum

            while queue and prefix_sum[i] - prefix_sum[queue[0]] >= k:
                l = queue.popleft()
                ans = min(ans, i-l)
            
            while queue and prefix_sum[i] <= prefix_sum[queue[-1]]:
                queue.pop()
            
            queue.append(i)
            if i<n:
                cur_sum += nums[i]
        
        return ans if ans!=float('inf') else -1