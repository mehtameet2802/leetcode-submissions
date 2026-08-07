class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        ans = 0
        for i,num in enumerate(nums):
            left = lower - num
            right = upper - num

            l = bisect_left(nums, left, i+1)
            r = bisect_right(nums, right, i+1)

            ans += (r-l)
        
        return ans