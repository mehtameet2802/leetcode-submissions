class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # '''
        # Pattern - QuickSelect
        # TC - O(n), worst O(n^2)
        # SC - O(1) - this is iterative, if recursive then worst - O(n), avg O(log n)
        # '''
        

        # target = len(nums) - k

        # def compare(a,b):
        #     if len(a) != len(b):
        #         return len(a)<=len(b)
        #     return a<=b

        # def partition(left, right):
        #     i = left

        #     pivot_idx = random.randint(left, right)
        #     nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

        #     pivot = nums[right]

        #     for j in range(left,right):
        #         if compare(nums[j],pivot):
        #             nums[i], nums[j] = nums[j], nums[i]
        #             i += 1
            
        #     nums[i], nums[right] = nums[right], nums[i]
        #     return i
        

        # def quickSelect(left, right):
        #     if left>=right:
        #         return

        #     pivot = partition(left, right)

        #     if pivot == target:
        #         return
        #     elif pivot < target:
        #         quickSelect(pivot+1, right)
        #     else:
        #         quickSelect(left, pivot-1)
        
        # quickSelect(0, len(nums)-1)
        # return nums[target]

        nums.sort(key = lambda x: (len(x),x))
        return nums[len(nums)-k]