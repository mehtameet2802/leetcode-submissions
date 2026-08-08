class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        '''
        Pattern - Backtracking

        TC - O(n * Catalan(n)), worst - O(2^(2n))
        SC - O(n) auxiliary
             O(n * Catalan(n)) including output - Catalan strings and each string has n characters
        '''
        
        ans = []

        def backtrack(cur, open_cnt, close_cnt):
            if len(cur) == 2*n:
                ans.append(cur)
                return
            
            if open_cnt < n:
                backtrack(
                    cur + '(',
                    open_cnt + 1,
                    close_cnt
                )
            
            if close_cnt < open_cnt:
                backtrack(
                    cur + ')',
                    open_cnt,
                    close_cnt + 1
                )
        
        backtrack("",0,0)
        return ans