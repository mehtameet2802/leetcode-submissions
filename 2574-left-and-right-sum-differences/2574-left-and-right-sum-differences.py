class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        pre_sum = 0
        total = sum(nums)

        for num in nums:
            diff = abs(pre_sum - (total-pre_sum-num))
            pre_sum += num
            ans.append(diff)
        
        return ans