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

        stack = []
        n = len(nums)
        ans = [-1]*n
        

        for i in range(2*n):
            idx = i % n

            while stack and nums[stack[-1]] < nums[idx]:
                j = stack.pop()
                ans[j] = nums[idx]
            
            if i < n:
                stack.append(i)
        
        return ans



        