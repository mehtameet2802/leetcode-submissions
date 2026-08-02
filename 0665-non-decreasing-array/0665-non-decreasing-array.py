class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)

        if n==1:
            return True
        
        cnt = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                cnt += 1
        
        if cnt > 1:
            return False
        
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                if cnt > 0:
                    if i > 0 and nums[i-1] > nums[i+1]:
                        nums[i+1] = nums[i]
                    else:
                        nums[i] = nums[i+1]
                    cnt -= 1
                else:
                    return False
        
        return True
