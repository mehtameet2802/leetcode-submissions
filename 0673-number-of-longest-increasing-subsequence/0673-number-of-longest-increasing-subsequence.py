class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        dp = [1]*len(nums)
        cnt = [1]*len(nums)
        n = len(nums)

        max_length = 1

        for i in range(1,n):
            cur_max = 1
            for j in range(i-1,-1,-1):
                if nums[j] >= nums[i]:
                    continue
                
                if dp[j] + 1 == cur_max:
                    cnt[i] += cnt[j]
                elif dp[j] + 1 > cur_max:
                    cur_max = dp[j]+1
                    dp[i] = cur_max
                    cnt[i] = cnt[j]  

            max_length = max(dp[i], max_length)

        ans = 0

        for i, val in enumerate(cnt):
            if dp[i] == max_length:
                ans += cnt[i]

        return ans