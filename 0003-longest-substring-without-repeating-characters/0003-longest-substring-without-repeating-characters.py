class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            cur_ch = s[right]

            if cur_ch in seen:
                left = max(left, seen[cur_ch]+1)
            
            max_length = max(max_length, right - left + 1)

            seen[cur_ch] = right

        return max_length