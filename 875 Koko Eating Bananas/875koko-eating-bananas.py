import sys
class Solution:
    ans = sys.maxsize
    def bin(self,s,e,arr,h):
        while s<=e:
            mid = int(s+(e-s)/2)
            a1 = 0
            for i in range(len(arr)):
                if arr[i]<=mid:
                    a1+=1
                else:
                    a1+=int((arr[i]+mid-1)/mid)
            
            if a1>h:
                s = mid+1
            elif a1<=h:
                self.ans = min(self.ans,mid)
                e = mid-1

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        piles.sort()
        s = 1
        e = piles[n-1]
        self.bin(s,e,piles,h)
        return self.ans