class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        counter_s = defaultdict(int)
        ans = s

        if len(s) < len(t) or Counter(s) & counter_t != counter_t:
            return ""

        left = 0

        for right in range(len(s)):
            counter_s[s[right]] += 1

            while Counter(counter_s) & counter_t == counter_t:
                if right - left + 1 < len(ans):
                    ans = s[left:right+1]
                counter_s[s[left]] -= 1
                left += 1
        
        return ans

            
