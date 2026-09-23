class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n < 3:
            return max(nums)

        first = nums[-1]
        second = max(nums[-1],nums[-2])

        for i in range(n-3,-1,-1):
            cur = max(second, nums[i] + first)
            first = second
            second = cur
        
        return second