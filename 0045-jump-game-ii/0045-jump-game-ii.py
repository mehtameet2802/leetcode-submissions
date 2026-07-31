class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        Pattern - Greedy

        TC - O(n)
        SC - O(1)
        '''

        n = len(nums)
        cnt = 0
        right = 0
        left = 0
        while right < n-1:

            farthest = 0
            
            for i in range(left,right+1):
                farthest = max(farthest,i+nums[i])
            
            left = right+1
            right = farthest
            cnt+=1
        
        return cnt