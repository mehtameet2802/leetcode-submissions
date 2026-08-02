class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        Pattern - Prefix Sum

        TC - O(N)
        SC - O(N)
        '''

        idx_map = {}
        
        prefix = 0
        ans = 0
        idx_map[0] = -1
        for i,num in enumerate(nums):
            if num == 0:
                prefix -= 1
            else:
                prefix += 1

            if prefix in idx_map:
                ans = max(ans,i-idx_map[prefix])
            else:
                idx_map[prefix] = i  
        
        return ans