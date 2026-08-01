class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = -1
        for num in nums:
            if nums[abs(num)-1]<0:
                duplicate = abs(num)
                continue
            nums[abs(num)-1] = -nums[abs(num)-1]
        
        ans = [duplicate]
        for i,num in enumerate(nums):
            if num>0:
                ans.append(i+1)

        if len(ans)<2:
            ans.append(len(nums))
        
        return ans