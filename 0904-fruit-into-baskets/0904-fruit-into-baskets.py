class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        '''
        Pattern - Sliding Window
        
        TC - O(N)
        SC - O(1)
        '''

        f_map = defaultdict(int)
        ans = 0
        left = 0
        k = 2

        for right in range(len(fruits)):
            f_map[fruits[right]] += 1

            while len(f_map) > k:
                f_map[fruits[left]] -= 1

                if f_map[fruits[left]] == 0:
                    del f_map[fruits[left]]

                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans