class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        '''
        Pattern - Sort + Scan

        TC - O(N*(M log M))
        SC - O(1)
        '''

        ans = []

        for s, e in zip(l,r):
        
            arr = nums[s:e+1]
            arr.sort()
            diff = arr[1] - arr[0]
            res = True

            for i in range(2,len(arr)):
                if arr[i] - arr[i-1] != diff:
                    res = False
                    break
            
            ans.append(res)
            
        return ans
