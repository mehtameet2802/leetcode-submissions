class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        '''
        recursive approach
        '''

        # words.sort(key=len)
        # words_set = set(words)

        # dp = {}

        # ans = 0

        # def helper(word):

        #     if word in dp:
        #         return dp[word]
            
        #     longest_after = 0
        #     n = len(word)
        #     for i in range(n+1):
        #         for j in range(26):
        #             new_word = word[0:i]+chr(j+ord('a'))+word[i:n]
                    
        #             if new_word in words_set:
        #                 longest_after = max(longest_after,helper(new_word))
            
        #     dp[word] = longest_after+1
        #     return longest_after+1

        # for word in words:
        #     ans = max(ans, helper(word))
        
        # return ans


        '''
        iterative 1d approach
        '''

        words.sort(key=len)

        dp = defaultdict(int)

        ans = 0

        def helper(word):
            longest_after = 0
            n = len(word)
            for i in range(n+1):
                for j in range(26):
                    new_word = word[0:i]+chr(j+ord('a'))+word[i:n]
                    longest_after = max(longest_after, dp[new_word])
            
            dp[word] = longest_after+1
            return longest_after+1

        for i in range(len(words)-1,-1,-1):
            ans = max(ans, helper(words[i]))
        
        return ans
                    
