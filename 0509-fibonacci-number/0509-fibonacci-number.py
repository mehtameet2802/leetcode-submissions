class Solution:
    def fib(self, n: int) -> int:
        f0 = 0
        f1 = 1
        f2 = 1

        arr = [0,1,1]

        for i in range(3,n+1):
            f_n = f2 + f1
            f0 = f1
            f1 = f2
            f2 = f_n

        if n < 2:
            return n
        
        return f2