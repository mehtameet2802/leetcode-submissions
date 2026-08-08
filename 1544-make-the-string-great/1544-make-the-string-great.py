class Solution:
    def makeGood(self, s: str) -> str:
        '''
        Pattern - Stack Simulation
        TC - O(N)
        SC - O(N)
        '''

        stack = []
        n = len(s)

        for i, ch in enumerate(s):
            if stack:
                if (
                    ch.lower() == stack[-1].lower()
                    and 
                    (
                        (stack[-1].islower() and ch.isupper()) or
                        (stack[-1].isupper() and ch.islower())
                    )
                ):
                    stack.pop()
                    continue

            
            stack.append(ch)
        
        return "".join(stack)
            