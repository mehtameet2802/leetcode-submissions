class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True
        
        r = len(nums)-2

        arr = [0]*len(nums)
        arr[-1] = 1

        target = r+1
        ans = False

        while r>=0:
            if nums[r]+r>=target:
                target = r
                arr[r] = 1
            else:
                arr[r]=0

            r-=1

        return True if arr[0]==1 else False