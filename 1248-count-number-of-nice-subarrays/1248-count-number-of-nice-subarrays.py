class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        '''
        Pattern - Prefix Sum

        TC - O(N)
        SC - O(k) - number of frequent odd numbers
        '''
        
        seen = defaultdict(int)

        seen[0] = 1

        prefix = 0
        ans = 0
        for num in nums:
            
            if num % 2 != 0:
                prefix += 1
            ans += seen[prefix-k]
            seen[prefix] += 1
            
        return ans

