class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        '''
        Pattern - 2 pointers (Fix Wrong Position)

        TC - O(N)
        SC - O(1)
        '''
        
        even = 0
        odd = 1
        n = len(nums)

        while even < n and odd < n:
            
            if nums[even] % 2 == 0:
                even += 2
            
            elif nums[odd] % 2 == 1:
                odd += 2

            else:
                nums[even], nums[odd] = nums[odd], nums[even]

                odd += 2
                even += 2 

        return nums