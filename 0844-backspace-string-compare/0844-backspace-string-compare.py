class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        '''
        Pattern - Stack (Simulation)

        TC - O(n)
        SC - O(n)
        '''
        stack = []

        for ch in s:
            if ch == '#' and stack:
                stack.pop()
                continue
            elif ch == '#':
                continue
            stack.append(ch)
        
        s = "".join(stack)
        stack = []

        for ch in t:
            if ch=='#' and stack:
                stack.pop()
                continue
            elif ch == '#':
                continue
            stack.append(ch)
        
        t = "".join(stack)

        return s == t