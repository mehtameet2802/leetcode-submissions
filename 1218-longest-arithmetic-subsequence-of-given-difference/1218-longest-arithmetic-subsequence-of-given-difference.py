class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # n = len(arr)
        # dp = [1]*n

        # for i in range(n):
        #     for j in range(i):
        #         if i>0 and arr[i] - arr[j] == difference:
        #             dp[i] = max(dp[i], dp[j]+1)

        # return max(dp) 

        dp = {}

        for num in arr:
            dp[num] = dp.get(num-difference,0) + 1

        return max(dp.values())