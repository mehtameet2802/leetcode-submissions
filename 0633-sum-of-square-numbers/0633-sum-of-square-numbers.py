class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 2:
            return True
        
        l = 0
        r = int(pow(c,0.5))

        while l<=r:
            cur = pow(l,2) + pow(r,2)
            if cur == c:
                return True
            elif cur>c:
                r-=1
            else:
                l+=1
        
        return False