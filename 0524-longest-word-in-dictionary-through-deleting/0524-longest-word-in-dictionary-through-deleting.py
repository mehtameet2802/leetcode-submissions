class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        ans = ""

        for word in dictionary:
            if len(s) < len(word):
                continue
            
            l = 0
            r = 0

            while l<len(s) and r<len(word):
                if s[l] == word[r]:
                    r += 1
                l += 1
            
            if r >= len(word):
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word

        return ans 
