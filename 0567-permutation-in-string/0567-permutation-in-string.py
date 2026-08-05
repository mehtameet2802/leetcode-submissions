class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr_s1 = [0]*26

        for ch in s1:
            arr_s1[ord(ch)-ord('a')] += 1
        

        left = 0
        arr_s2 = [0]*26

        for right in range(len(s2)):
            arr_s2[ord(s2[right])-ord('a')] += 1

            if right - left + 1 == len(s1):
                if arr_s2 == arr_s1:
                    return True
                
                arr_s2[ord(s2[left])-ord('a')] -= 1
                left += 1

        return False