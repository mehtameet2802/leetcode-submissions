from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        f_map = Counter(answers)

        ans = 0

        for value, f in f_map.items():
            ans += ceil(f/(value+1)) * (value+1)

        return ans
