class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # k = len(nums)
        # nums += nums
        # stack = []

        # print(nums)

        # for i in range(len(nums)):
        #     j = i
        #     while j < i+k and stack and nums[stack[-1]] <= nums[i]:
        #         t = stack.pop()
        #         nums[t] = nums[i]
        #         j += 1
            
        #     stack.append(i)
        
        # return nums[:k]

        n = len(nums)
        ans = [-1] * n
        stack = []

        # Traverse the array twice.
        #
        # First pass:
        #   Find normal next greater elements.
        #
        # Second pass:
        #   Allows elements near the end to find
        #   a greater element near the beginning.
        for i in range(2 * n):

            idx = i % n

            # Current element is greater than the
            # unresolved elements on the stack.
            while stack and nums[stack[-1]] < nums[idx]:
                j = stack.pop()
                ans[j] = nums[idx]

            # Only put indices from the ORIGINAL array
            # into the stack.
            #
            # We don't need to push during the second
            # occurrence of the same index.
            if i < n:
                stack.append(idx)

        return ans


        