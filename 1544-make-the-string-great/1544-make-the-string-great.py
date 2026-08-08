class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        n = len(s)

        for i, ch in enumerate(s):
            if stack and stack[-1][0]>=0 and stack[-1][0]<=n-2:
                if (
                    ch.lower() == stack[-1][1].lower()
                    and 
                    (
                        (stack[-1][1].islower() and ch.isupper()) or
                        (stack[-1][1].isupper() and ch.islower())
                    )
                ):
                    stack.pop()
                    continue

            
            stack.append((i,ch))

        ans = []
        for i,ch in stack:
            ans.append(ch)
        
        return "".join(ans)
            