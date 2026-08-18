class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        cnt = [1]*n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j]+1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
        
        max_len = max(dp)
        ans = 0
        for l,c in zip(dp,cnt):
            if l == max_len:
                ans += c
        return ans
                    
                    

