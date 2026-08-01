class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        
        nums.sort()
        ans = float('inf')
        diff = float('inf')

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1
            find = target - nums[i] 
            

            while l<r:
                d1 = find - nums[l] - nums[r] 
                if nums[l] + nums[r] < find:
                    l+=1                    
                elif nums[l] + nums[r] > find:
                    r-=1
                else:
                    return target

                if abs(d1) < diff:
                    diff = abs(d1)
                    ans = target - d1
            
        
        return ans
