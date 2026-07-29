class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        ans = 0

        for right in range(len(s)):

            if s[right] in last_seen:
                left = max(left,last_seen[s[right]]+1)
            
            last_seen[s[right]] = right
            ans = max(ans, right-left+1)

        return ans