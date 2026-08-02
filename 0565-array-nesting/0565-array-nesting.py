class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        seen = set()

        ans = 0

        for i in range(len(nums)):
            if i not in seen:
                cur = i
                length = 0
                while cur not in seen:
                    seen.add(cur)
                    cur = nums[cur]
                    length += 1
                ans = max(ans, length)
            

        return ans