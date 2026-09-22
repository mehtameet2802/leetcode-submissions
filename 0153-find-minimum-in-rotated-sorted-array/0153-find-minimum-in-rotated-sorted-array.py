class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left<=right:
            mid = left + (right - left)//2

            if nums[left] <= nums[mid] and nums[right] < nums[mid]:
                if mid+1<=right and nums[mid+1] < nums[mid]:
                    return nums[mid+1]
                else:
                    left = mid + 1
            else:
                if mid-1>=left and nums[mid-1] > nums[mid]:
                    return nums[mid]
                else:
                    right = mid - 1
        
        return nums[left]