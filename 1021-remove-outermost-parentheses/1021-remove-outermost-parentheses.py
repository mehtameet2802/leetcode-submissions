class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open = 0
        skipped = 0
        stack = []

        for ch in s:
            if open == 0 and skipped == 0 and ch == '(':
                skipped += 1
                continue
            
            if open == 0 and skipped == 1 and ch == ')':
                skipped -= 1
                continue
            
            if open>0 and ch == ')':
                open -= 1
            else:
                open += 1
            
            stack.append(ch)
        
        return "".join(stack)

