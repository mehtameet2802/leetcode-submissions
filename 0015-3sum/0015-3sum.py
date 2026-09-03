class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # '''
        # pseudo code
        # ans = []
        # iterate through the nums
        # for idx in nums:
            
        #     target = 0 - num[idx]
        #     seen - a set for maintaining seen numbers

        #     for j in nums[idx+1] to nums[n]:
        #         if target - j in seen:
        #             ans.append[[nums[i],nums[j],nums[k]]]
        #             break
                
        #         seen.add(nums[j])
        
        # return ans

        # in first run used list instead of set and did not sort so got duplicates,
        # used break so did not get all the set
        # did not sort 

        # TC - O(n^2)
        # SC - O(n)


        # '''

        # nums.sort()

        # ans = set()
        # n = len(nums)

        # for idx1 in range(n):
        #     target = 0 - nums[idx1]
        #     seen = set()

        #     for idx2 in range(idx1+1,n):

        #         if (target - nums[idx2]) in seen:
        #             ans.add((nums[idx1],nums[idx2],target-nums[idx2]))
        #             # break
                
        #         seen.add(nums[idx2])
        
        # return list(ans)

        nums.sort()
        ans = []
        n = len(nums)
        for first in range(n-2):

            if first>0 and nums[first] == nums[first-1]:
                continue
            
            left = first + 1
            right = n - 1

            while left < right:
                cur_sum = nums[first] + nums[left] + nums[right]

                if cur_sum > 0: 
                    right -= 1
                elif cur_sum < 0:
                    left += 1
                else:
                    ans.append([nums[first],nums[left],nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
            
        return ans

