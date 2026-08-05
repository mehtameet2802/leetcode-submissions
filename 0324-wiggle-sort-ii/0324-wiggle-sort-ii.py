class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        '''
        Pattern - 

        TC - O(N log N)
        SC - O(N)
        '''
        
        arr = sorted(nums)

        n = len(nums)
        half = (n+1) // 2
        i = half - 1
        j = n - 1

        for k in range(n):
            if k % 2 == 0:
                nums[k] = arr[i]
                i -= 1
            else:
                nums[k] = arr[j]
                j -= 1
        