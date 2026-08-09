class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)

        ans = 0
        for i in range(n):
            steps = 0

            while stack and stack[-1][0] <= nums[i]:
                val, prev_steps = stack.pop()
                steps = max(steps,prev_steps)

            if stack:
                steps += 1

            ans = max(ans,steps)

            stack.append((nums[i],steps))
        
        return ans

