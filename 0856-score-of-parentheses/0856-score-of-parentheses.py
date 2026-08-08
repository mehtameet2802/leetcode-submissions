class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for ch in s:
            if ch == '(':
                stack.append('(')
            else:
                cur = 0
                while stack and stack[-1] != '(':
                    ele = stack.pop()
                    cur += ele

                stack.pop()
                if cur > 0:
                    stack.append(2*cur)
                else:
                    stack.append(1)
        
        return sum(stack)