class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        n = len(nums)
        k = k % n

        if k==0:
            return

        nums[:] = nums[::-1]
        print(nums)
        nums[:k] = nums[k-1::-1]
        nums[k:] = nums[:k-1:-1]