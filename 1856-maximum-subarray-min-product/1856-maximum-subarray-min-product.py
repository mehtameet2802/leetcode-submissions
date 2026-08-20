class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = [0]*(n+1)

        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        stack = []
        ans = 0

        for i in range(n+1):
            curr = nums[i] if i < n else 0

            while stack and nums[stack[-1]] >= curr:

                j = stack.pop()

                left = stack[-1] if stack else -1
                right = i

                total = prefix[right] - prefix[left+1]

                ans = max(ans, total*nums[j])

            if i < n:
                stack.append(i)
        return ans % (10**9 + 7)