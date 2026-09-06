class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = [0] * 26
        counter_s2 = [0] * 26

        for ch in s1:
            counter_s1[ord(ch)-ord('a')] += 1

        k = len(s1)

        left = 0

        for right, ch in enumerate(s2):
            counter_s2[ord(ch)-ord('a')] += 1

            while (right - left + 1) > k:
                counter_s2[ord(s2[left])-ord('a')] -= 1
                left += 1
            
            if counter_s1 == counter_s2:
                return True
        
        return False
