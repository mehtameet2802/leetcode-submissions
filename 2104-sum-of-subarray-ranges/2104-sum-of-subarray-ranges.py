class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        left = [0]*n
        right = [0]*n

        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()

            if stack:
                left[i] = i - stack[-1]
            else:
                left[i] = i+1

            stack.append(i)
        
        stack = []
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            
            if stack:
                right[i] = stack[-1] - i
            else:
                right[i] = n - i

            stack.append(i)
        
        min = 0
        for i in range(n):
            min += nums[i] * left[i] * right[i]
        
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            
            if stack:
                left[i] = i - stack[-1]
            else:
                left[i] = i + 1

            stack.append(i)
        
        stack = []
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            
            if stack:
                right[i] = stack[-1] - i
            else:
                right[i] = n - i

            stack.append(i)
        
        max = 0
        for i in range(n):
            max += nums[i] * left[i] * right[i]

        return max - min
