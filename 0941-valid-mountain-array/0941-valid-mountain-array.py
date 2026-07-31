class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n<3:
            return False

        i = 0
        cnt = 1
        while i<n-1:
            if arr[i]<arr[i+1]:
                i+=1
                cnt += 1
                continue
            break
        
        if i == n-1:
            return False

        cnt = 1
        while i<n-1:
            if arr[i]>arr[i+1]:
                i+=1
                cnt+=1
                continue
            break
            
        return i == n-1 and cnt!=n

