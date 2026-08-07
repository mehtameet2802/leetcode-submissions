class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        '''
        Pattern - Stack (Simulation)

        TC - O(len(s) + len(t))
        SC - O(max(len(s),len(t)))
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