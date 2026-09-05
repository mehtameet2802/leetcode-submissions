class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        counter_s = defaultdict(int)
    
        # if len(s) < len(t) or Counter(s) & counter_t != counter_t:
        #     return ""

        left = 0
        best_left = 0
        best_length = float('inf')
        formed = 0

        for right in range(len(s)):
            right_ch = s[right]
            counter_s[right_ch] += 1

            if right_ch in counter_t and counter_s[right_ch] == counter_t[right_ch]:
                formed += 1

            while formed == len(counter_t):
                window_len = right - left + 1
                
                if window_len < best_length:
                    best_left = left
                    best_length = window_len
                
                left_ch = s[left]
                

                if left_ch in counter_t and counter_s[left_ch] <= counter_t[left_ch]:
                    formed -= 1

                counter_s[left_ch] -= 1
                left += 1
        
        if best_length == float('inf'):
            return ""

        return s[best_left:best_left + best_length]

            
