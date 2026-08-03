class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)

        seen[0] = 1

        cnt = 0
        ans = 0
        for num in nums:
            
            if num % 2 != 0:
                cnt += 1
            seen[cnt] += 1
            ans += seen[cnt-k]

        return ans

