class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if stack:
                ele = stack[-1]
                if ch==')' and ele=='(' or ch=='}' and ele =='{' or ch==']' and ele=='[':
                    stack.pop()
                    continue
            stack.append(ch)
        
        if stack:
            return False
        return True
