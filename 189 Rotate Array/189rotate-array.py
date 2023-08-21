class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%(len(nums))
        n = len(nums)
        k = n-k
        n1 = []
        for i in range(k,n):
            n1.append(nums[i])
        
        for i in range(0,k):
            n1.append(nums[i])
        
        nums[:] = n1