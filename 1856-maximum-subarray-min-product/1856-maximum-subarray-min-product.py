class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = [0]*n
        prefix[0] = nums[0]

        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
        
        stack = []
        ans = 0

        for i in range(n):
            curr = nums[i] if i < n else 0

            while stack and nums[stack[-1]] >= curr:

                j = stack.pop()

                left = stack[-1] if stack else -1
                right = i

                if left == -1:
                    total = prefix[right-1]
                else:
                    total = prefix[right-1] - prefix[left]

                ans = max(ans, total*nums[j])

            stack.append(i)

        while stack:
            j = stack.pop()
            left = stack[-1] if stack else -1
            right = n

            if left == -1:
                    total = prefix[right-1]
            else:
                total = prefix[right-1] - prefix[left]

            ans = max(ans, total*nums[j])

        
        return ans % (10**9 + 7)