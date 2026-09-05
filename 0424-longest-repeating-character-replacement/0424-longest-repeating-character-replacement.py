class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        highest_ele = s[0]
        highest_freq = 0
        arr = [0]*26
        ans = 0

        left = 0
        right = 0

        while right < len(s):

            arr[ord(s[right]) - ord('A')] += 1
            if arr[ord(s[right]) - ord('A')] > highest_freq:
                highest_freq = arr[ord(s[right]) - ord('A')]
                highest_ele = s[right]

            window_len = right-left+1
            
            while window_len - highest_freq > k:
                arr[ord(s[left]) - ord('A')] -= 1
                window_len -=1
                left += 1
                
            ans = max(ans,window_len)

            right += 1

        return ans
            


