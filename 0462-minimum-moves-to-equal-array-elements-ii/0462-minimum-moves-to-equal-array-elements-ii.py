class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        target = len(nums)//2

        def partition(left, right):

            i = left
            pivot = nums[right]

            for j in range(left,right):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            
            nums[i], nums[right] = nums[right], nums[i]
            return i
        
        def quickSelect(left,right):

            pivot = partition(left,right)

            if pivot == target:
                return nums[pivot]
            elif pivot < target:
                return quickSelect(pivot+1,right)
            else:
                return quickSelect(left, pivot-1)

        median = quickSelect(0,len(nums)-1)

        total = 0
        for num in nums:
            total += abs(median-num)
        
        return total
