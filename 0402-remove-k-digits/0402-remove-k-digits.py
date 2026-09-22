class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        if k >= len(num):
            return "0"

        for i, ch in enumerate(num):            
            while k>0 and stack and int(stack[-1]) > int(ch):
                stack.pop()
                k-=1
            
            if not stack and ch == '0':
                continue
            
            stack.append(ch)
        

        while stack and k>0:
            stack.pop()
            k-=1

        if not stack:
            return "0"

        return "".join(stack)

