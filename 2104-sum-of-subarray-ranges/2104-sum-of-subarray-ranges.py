class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        stack = []
        ans = 0

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                ele_idx = stack.pop()
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                
                right = i

                left_span = ele_idx - left
                right_span = right - ele_idx

                ans += nums[ele_idx] * left_span * right_span
            
            stack.append(i)

        
        while stack:
            ele_idx = stack.pop()
            if stack:
                left = stack[-1]
            else:
                left = -1
            
            right = len(nums)

            left_span = ele_idx - left
            right_span = right - ele_idx

            ans += nums[ele_idx] * left_span * right_span

        stack = []
        ans = -ans

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                ele_idx = stack.pop()
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                
                right = i

                left_span = ele_idx - left
                right_span = right - ele_idx

                ans += nums[ele_idx] * left_span * right_span
            
            stack.append(i)

        while stack:
            ele_idx = stack.pop()
            if stack:
                left = stack[-1]
            else:
                left = -1
            
            right = len(nums)

            left_span = ele_idx - left
            right_span = right - ele_idx

            ans += nums[ele_idx] * left_span * right_span

        return ans
