class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0

        for num in nums:
            if num==0:
                cnt0+=1
            elif num==1:
                cnt1+=1
            else:
                cnt2+=1
        
        i=0
        while i<len(nums) and cnt0>0:
            nums[i] = 0
            i+=1
            cnt0-=1
        
        while i<len(nums) and cnt1>0:
            nums[i] = 1
            i+=1
            cnt1-=1
        
        while i<len(nums) and cnt2>0:
            nums[i] = 2
            i+=1
            cnt2-=1
