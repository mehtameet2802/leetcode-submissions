class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # '''
        # Pattern - Stack / Parentheses Depth

        # TC - O(N)
        # SC - O(N)
        # '''

        # open = 0
        # skipped = 0
        # stack = []

        # for ch in s:
        #     if open == 0 and skipped == 0 and ch == '(':
        #         skipped += 1
        #         continue
            
        #     if open == 0 and skipped == 1 and ch == ')':
        #         skipped -= 1
        #         continue
            
        #     if open>0 and ch == ')':
        #         open -= 1
        #     else:
        #         open += 1
            
        #     stack.append(ch)
        
        # return "".join(stack)


        '''
        Pattern - Stack / Parentheses Depth

        TC - O(N)
        SC - O(N)
        '''

        depth = 0
        ans = []

        for ch in s:
            if ch == '(':
                if depth > 0:
                    ans.append(ch)
                
                depth += 1
            else:
                depth -= 1
                
                if depth > 0:
                    ans.append(ch)
                
                
        
        return "".join(ans)



