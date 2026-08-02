from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)

        prefix = 0
        ans = 0

        seen[0] = 1

        for num in nums:
            prefix += num
            
            ans += seen[prefix-k]
            
            seen[prefix] += 1
        
        return ans