class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        Pattern - Upper + Lower Bound
        TC - O(log n)
        SC - O(1)
        '''
        
        if not nums:
            return [-1,-1]

        if target > nums[-1] or target < nums[0]:
            return [-1, -1]

        l = 0
        r = len(nums)
        ans = []

        while l < r:

            mid = l + (r-l)//2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        if nums[l] == target:
            ans.append(l)
        else:
            ans.append(-1)
        
        l = 0
        r = len(nums)

        while l < r:

            mid = l + (r-l)//2

            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
            
        if nums[l-1] == target:
            ans.append(l-1)
        else:
            ans.append(-1)
        
        return ans


        