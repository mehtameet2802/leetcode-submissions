class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True
        
        r = len(nums)-2

        target = r+1
        ans = False

        while r>=0:
            if nums[r]+r>=target:
                target = r
                ans = True
            else:
                ans = False

            r-=1

        return ans