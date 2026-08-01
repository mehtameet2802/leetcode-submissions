class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        Pattern - Sorting + 2 Pointer
        TC - 
        SC - 
        '''

        nums.sort()
        ans = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):

                l = j+1
                r = len(nums)-1

                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                
                find = target - nums[i] - nums[j] 
                while l<r:
                    if nums[l] + nums[r] > find:
                        r -= 1
                    elif nums[l] + nums[r] < find:
                        l+=1
                    else:

                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1

                        while l<r and nums[l] == nums[l-1]:
                            l+=1
                        
                        while l<r and nums[r] == nums[r+1]:
                            r-=1
        
        return ans