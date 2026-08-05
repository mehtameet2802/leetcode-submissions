class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        '''
        Pattern - Sliding Window

        TC - O(N)
        SC - O(1)
        '''
        
        arr = [0]*26
        left = 0
        ans = 0

        for right in range(len(s)):
            ch_idx = ord(s[right]) - ord('a')
            
            arr[ch_idx] += 1
            
            while arr[ch_idx] > 2:
                arr[ord(s[left]) - ord('a')] -= 1
                left += 1
                
            ans = max(ans, right - left + 1)

        return ans