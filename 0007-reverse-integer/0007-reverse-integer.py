class Solution:
    def reverse(self, x: int) -> int:
        s1 = 0
        if x<0:
            s1 = 1
        num1 = list(str(x))
        num1.reverse()
        num2 = ""
        for i in num1:
            if i>='0' and i<='9':
                num2+=i
        num2 = int(num2)
        if s1:
            num2 = -1*num2
        
        if num2>(2**31-1) or num2<(-(2**31)):
            return 0
        return num2