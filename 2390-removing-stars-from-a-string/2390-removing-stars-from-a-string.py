class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == '*':
                if stack:
                    stack.pop()
                    continue
            stack.append(ch)

        return "".join(stack)