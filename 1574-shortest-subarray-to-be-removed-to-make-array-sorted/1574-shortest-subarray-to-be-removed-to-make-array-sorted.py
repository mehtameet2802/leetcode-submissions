class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        s = 0
        n = len(arr)
        while s<n-1 and arr[s]<=arr[s+1]:
            s+=1
        
        if s==n-1:
            return 0

        e = len(arr)-1
        while e>0 and arr[e]>=arr[e-1]:
            e-=1
        
        ans = min(n-s-1,e)

        i = 0
        j = e

        while i<=s and j<n:
            if arr[i]<=arr[j]:
                ans = min(ans,j-i-1)
                i+=1
            else:
                j+=1
        
        return ans