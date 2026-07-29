import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        """
        Pattern - Binary Search

        Time Complexity - O(log n)
        Space Complexity - 0

        """
        
        # l = 0
        # r = len(nums)-1



        # while l<=r:
        #     mid = l + (r-l)//2

        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid]<target:
        #         l = mid+1
        #     else:
        #         r = mid-1
        
        # return -1

        ind = bisect.bisect_left(nums, target)

        if ind<len(nums) and nums[ind] == target:
            return ind
        
        return -1

