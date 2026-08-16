class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        '''
        TC - O(N*2^N)
        SC - O(N)
        '''
        ans = 0
        values = []

        def xor():
            val = 0
            for num in values:
                val = val ^ num
            
            return val
        
        def subsets(i):
            nonlocal ans
            ans += xor()
            
            for j in range(i, len(nums)):
                values.append(nums[j])
                subsets(j+1)
                values.pop()
            
        subsets(0)
        return ans