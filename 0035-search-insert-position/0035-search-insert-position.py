class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        Pattern - Lower Bound

        TC - O(log n)
        SC - O(1)
        '''

        l = 0
        r = len(nums)

        while l < r:
            mid = l + (r-l)//2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        return l