class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        Pattern - Binary Search - go towards the direction where the uphill is increasing
        TC - O(log n)
        SC - O(1)
        '''

        l = 0
        r = len(nums) - 1

        while l< r:
            mid = l + (r-l)//2

            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid

        return l


