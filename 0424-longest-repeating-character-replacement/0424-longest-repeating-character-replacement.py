class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        left = 0
        right will come from for loop
        high_freq
        high_ele
        max_length
        arr - of len 26, to maintain freq
        every time in for loop a new ch comes, increment its freq
        window_len = right - left + 1
        if window_len - high_freq > k, start incrementing left, and each time decrement the freq of left ch
        once done update max length
        finally return max_length
        '''

        left = 0
        arr = [0]*26
        highest_freq = 0
        highest_ele = ""
        max_length = 0

        for right in range(len(s)):
            arr[ord(s[right]) - ord('A')] += 1

            if highest_freq < arr[ord(s[right]) - ord('A')]:
                highest_freq = arr[ord(s[right]) - ord('A')]
                highest_ele = s[right]

            window_len = right - left + 1
            while window_len - highest_freq > k:
                arr[ord(s[left]) - ord('A')] -= 1
                window_len -= 1
                left += 1
            
            max_len = max(max_length, window_len)
            
        return max_len