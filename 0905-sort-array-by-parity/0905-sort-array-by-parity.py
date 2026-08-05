class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        '''
        Pattern - Dutch National Flag/2 way Partitioning

        TC - O(N)
        SC - O(1)
        '''

        n = len(nums)
        L = 0
        R = n
        mid = 0

        while mid < R:
            if nums[mid] == 0:
                mid += 1
            elif nums[mid] % 2 == 0:
                nums[L], nums[mid] = nums[mid], nums[L]
                L += 1
                mid += 1
            elif nums[mid] % 2 == 1:
                nums[R-1], nums[mid] = nums[mid], nums[R-1]
                R -= 1
            

        return nums