from collections import Counter
from math import ceil

class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        '''
        Pattern - Greedy + Frequency Map

        TC - O(N)
        SC - O(U)   # U = number of unique answers
        '''

        f_map = Counter(answers)

        ans = 0

        for value, f in f_map.items():
            group_n = ceil(f / (value + 1))
            ans += group_n * (value + 1)

        return ans