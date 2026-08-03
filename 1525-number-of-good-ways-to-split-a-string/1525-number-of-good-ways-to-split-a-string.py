class Solution:
    def numSplits(self, s: str) -> int:
        splits = 0
        seen = set()

        n = len(s)

        pre = [0]*n
        suf = [0]*n

        for i in range(n):
            seen.add(s[i])
            pre[i] = len(seen)

        seen.clear()
        for i in range(n-1,-1,-1):
            seen.add(s[i])
            suf[i] = len(seen)
        
        for i in range(n-1):
            if pre[i] == suf[i+1]:
                splits += 1
        
        return splits