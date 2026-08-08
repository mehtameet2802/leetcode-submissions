class Solution:
    def calculate(self, s: str) -> int:
        # stack = []

        # opt = {
        #     '+': lambda a,b: a+b,
        #     '-': lambda a,b: a-b,
        #     '/': lambda a,b: int(a/b),
        #     '*': lambda a,b: a*b,
        # }

        # for ch in s:
        #     if ch == " ":
        #         continue
            
        #     stack.append(ch)
        
        # ele = stack.pop()

        # while stack:
        #     operator = stack.pop()
        #     ele = opt[operator](stack[-1], ele)
        #     stack.pop()
        
        # return ele

        stack = []
        num = 0
        sign = '+'

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            if ch in '+-*/' or i == len(s)-1:
                
                if sign == '+':
                    stack.append(num)
                
                elif sign == '-':
                    stack.append(-num)
                
                elif sign == '/':
                    stack[-1] = int(stack[-1]/num)
                
                else:
                    stack[-1] = stack[-1]*num
                
                sign = ch
                num = 0
        
        return sum(stack)
