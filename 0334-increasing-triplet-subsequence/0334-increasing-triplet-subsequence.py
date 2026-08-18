class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # n = len(nums)
        # dp = [1]*n

        # for i in range(n):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j]+1)

        #         if dp[i]==3:
        #             return True
        # return False

        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False