class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = defaultdict(int)
        counter_s2 = defaultdict(int)

        for ch in s1:
            counter_s1[ch] += 1

        k = len(s1)

        left = 0

        for right, ch in enumerate(s2):
            counter_s2[ch] += 1

            while (right - left + 1) > k:
                counter_s2[s2[left]] -= 1

                if counter_s2[s2[left]] == 0:
                    del counter_s2[s2[left]]

                left += 1
            
            if counter_s1 == counter_s2:
                return True
        
        return False
