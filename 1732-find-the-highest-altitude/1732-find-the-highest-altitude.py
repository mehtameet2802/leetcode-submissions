class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur = 0
        ans = 0

        for num in gain:
            cur = cur + num
            ans = max(ans, cur)
        
        return ans