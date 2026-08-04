class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        '''
        Pattern - 2 Pointer

        TC - O(N log N)
        SC - O(1)
        '''

        nums.sort()
        n = len(nums)
        ans = 0

        for i in range(n-1,1,-1):
            l = 0
            r = i-1

            while l<r:
                if nums[l] + nums[r] > nums[i]:
                    ans += (r-l)
                    r -= 1
                else:
                    l+=1
        
        return ans
