class Solution:
    def removeDuplicates(self, s: str) -> str:
        '''
        Pattern - Stack (Adjacent Cancellation)

        TC - O(n)
        SC - O(n)
        '''
       
        stack = []

        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
                continue
            stack.append(ch)
        
        return "".join(stack)