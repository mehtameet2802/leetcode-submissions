class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def cal(num):
            new_num = 0
            while num>0:
                new_num += pow(num%10,2)
                num = num//10
            return new_num


        while n not in seen:
            seen.add(n)
            if n == 1:
                return True
            n = cal(n)
        
        return False
