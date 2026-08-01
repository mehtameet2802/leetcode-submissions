class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # for i, num in enumerate(nums):
        #     nums[i] = pow(nums[i],2)
        
        # return sorted(nums)

        l = 0
        r = len(nums)-1

        ans = [0] * len(nums)
        i = r

        while l<=r:
            if abs(nums[l])>=abs(nums[r]):
                ans[i] = pow(nums[l],2)
                l+=1
            else:
                ans[i] = pow(nums[r],2)
                r-=1
            i-=1
        
        return ans