class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        '''
        Pattern - Sorting + 2 pointer

        TC - O(N^2)
        SC - O(1)
        '''

        if len(nums) == 3:
            return sum(nums)
        
        nums.sort()
        ans = float('inf')
        diff = float('inf')

        for i in range(len(nums)):
            
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
