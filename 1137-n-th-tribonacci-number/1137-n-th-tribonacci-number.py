class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1

        for i in range(3,n+1):
            tn = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = tn
        
        if n<2:
            return n

        return t2