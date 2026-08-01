class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Pattern - 2 pointer, fast & slow pointer

        TC - O(N)
        SC - O(1)
        '''

        w = 0
        r = 0

        while r<len(nums):
            if w>1 and nums[w-2] == nums[r]:
                r += 1
                continue
            
            nums[w] = nums[r]
            r += 1
            w += 1
        
        return w
