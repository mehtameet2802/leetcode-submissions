class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key=len)
        words_set = set(words)

        dp = {}

        ans = 0

        def helper(word):

            if word in dp:
                return dp[word]
            
            cnt = 0
            n = len(word)
            for i in range(n+1):
                for j in range(26):
                    new_word = word[0:i]+chr(j+ord('a'))+word[i:n]
                    
                    if new_word in words_set:
                        cnt = max(cnt,helper(new_word))
            
            dp[word] = cnt+1
            return cnt+1

        for word in words:
            ans = max(ans, helper(word))
        
        return ans
                    
