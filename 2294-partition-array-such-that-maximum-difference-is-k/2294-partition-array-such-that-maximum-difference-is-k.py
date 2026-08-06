class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        '''
        Pattern - Sort + Greedy

        TC - O(N log N)
        SC - O(1)
        '''

        partitions = 1

        nums.sort()
        
        start = nums[0]
        r = 0
        for i in range(len(nums)):
            if nums[i] - start > k:
                partitions += 1
                start = nums[i]

            
        return partitions