class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        num1 = list(str(x))
        num1.reverse()
        num2 = ""
        for i in num1:
            num2+=i
        
        if int(num2)==x:
            return True
        
        return False
