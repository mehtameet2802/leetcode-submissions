class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        agg = defaultdict(int)

        for num in nums:
            agg[num] = agg[num] + num
        
        prev2 = 0
        prev1 = agg[1]

        for i in range(2,max(nums)+1):
            cur = max(
                prev2 + agg[i],
                prev1
            )
            prev2 = prev1
            prev1 = cur
        
        return prev1