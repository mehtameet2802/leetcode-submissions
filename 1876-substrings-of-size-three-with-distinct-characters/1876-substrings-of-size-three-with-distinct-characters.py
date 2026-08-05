class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        '''
        Pattern - Fixed Window

        TC - O(N)
        SC - O(1)
        '''
        
        left = 0
        window = 3
        ans = 0
        seen = [0]*26

        for right in range(len(s)):

            if seen[ord(s[right])-ord('a')] > 0:
                while s[left] != s[right]:
                    seen[ord(s[left])-ord('a')] -= 1
                    left += 1
                seen[ord(s[left])-ord('a')] -= 1
                left += 1
                
            
            seen[ord(s[right])-ord('a')] += 1

            if right - left + 1 == window:
                ans += 1
                
                seen[ord(s[left])-ord('a')] -= 1
                left += 1

        return ans