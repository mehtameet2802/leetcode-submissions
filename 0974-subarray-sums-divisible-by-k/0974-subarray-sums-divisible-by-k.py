class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        '''
        Pattern - Prefix Sum +  Hash Map + Modulo

        TC - O(N)
        SC - O(k) - number of remainders that is 0 to k-1
        '''

        f_map = defaultdict(int)

        f_map[0] = 1
        ans = 0
        prefix = 0

        for num in nums:
            prefix += num 
            
            ans += f_map[prefix % k]

            f_map[prefix % k] += 1
        
        return ans