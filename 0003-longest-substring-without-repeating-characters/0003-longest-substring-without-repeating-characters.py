class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = [0] * 100

        left = 0
        max_length = -float('inf')

        for right in range(len(s)):
            if arr[ord(s[right])-ord('a')] == 0:
                arr[ord(s[right])-ord('a')] = 1
                continue
            
            max_length = max(max_length,right - left)
            while left < right and s[left] != s[right]:
                arr[ord(s[left])-ord('a')] = 0
                left += 1
            
            left += 1
            
        if max_length == -float('inf'):
            return len(s)
        else:
            max_length = max(max_length,right-left+1)

        return max_length

            
