class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Pattern - Binary Search
        TC - O(log n)
        SC - O(1)
        '''

        l = 0
        r = len(nums) - 1

        while l<=r:
            mid = l + (r-l)//2

            if nums[l] <= nums[mid] and nums[r]<nums[mid]:
                if mid + 1 <= r and nums[mid+1]<nums[mid]:
                    return nums[mid+1]
                else:
                    l = mid + 1
            else:
                if mid-1>=l and nums[mid-1]>nums[mid]:
                    return nums[mid]
                else:
                    r = mid - 1
        
        return nums[l]