class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        TC = O(N log N + N × K)
        K - can be 2^N

        SC = O(N)        ← auxiliary space
        SC = O(N × K)    ← including output
        '''
        ans = []
        path = []

        nums.sort()
        
        def subsets(i):
            ans.append(path.copy())

            for j in range(i, len(nums)):
                if j>i and nums[j-1] == nums[j]:
                    continue
                path.append(nums[j])
                subsets(j+1)
                path.pop()
            
        subsets(0)
        return ans