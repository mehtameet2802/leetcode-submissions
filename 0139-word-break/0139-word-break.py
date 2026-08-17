class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = {}

        def helper(i,length):
            if (i,length) in dp:
                return dp[(i,length)]
            
            if i == len(s):
                return length == 0
            
            ans = False
            if s[i-length:i+1] in wordDict:
                ans = helper(i+1,0)

            ans = ans or helper(i+1, length + 1)
            dp[(i,length)] = ans
            return ans

        return helper(0,0)  