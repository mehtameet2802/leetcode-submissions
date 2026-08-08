class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # stack = []

        # for i,ch in enumerate(num):
        #     while stack and int(stack[-1]) > int(ch) and k>0:
        #         stack.pop()
        #         k-=1
            
        #     if not stack and ch == "0":
        #         continue
        #     stack.append(ch)
        
        # while stack and k>0:
        #     stack.pop()
        #     k-=1
        
        # if not stack:
        #     stack.append("0")

        # return "".join(stack)


        stack = []

        for ch in num:
            while stack and int(stack[-1]) > int(ch) and k>0:
                stack.pop()
                k-=1
            stack.append(ch)
        
        while stack and k>0:
            stack.pop()
            k-=1

        ans = "".join(stack).lstrip('0')

        return ans if ans else "0"