class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        min_q = deque()
        max_q = deque()
        left = 0
        ans = 0

        for right, num in enumerate(nums):
            while min_q and nums[min_q[-1]] > num:
                min_q.pop()
            
            min_q.append(right)

            while max_q and nums[max_q[-1]] < num:
                max_q.pop()
            
            max_q.append(right)

            while min_q and max_q and abs(nums[min_q[0]] - nums[max_q[0]]) > limit:
                if min_q[0] == left:
                    min_q.popleft()
                
                if max_q[0] == left:
                    max_q.popleft()
                
                left += 1
            
            ans = max(ans,right - left + 1)

        return ans
