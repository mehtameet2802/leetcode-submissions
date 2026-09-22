class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        # stack = []
        # n = len(nums)
        # ans = [-1]*len(nums)

        # for i in range(2*n):

        #     num = nums[i%n]
        #     cur_idx = i%n

        #     if ans[cur_idx] != -1:
        #         continue
            
        #     while stack and stack[-1][0] < num:
        #         ele,idx = stack.pop()
        #         ans[idx] = num
            
        #     if not stack:
        #         stack.append((num,cur_idx))
        #         continue
            
        #     if stack and stack[-1][0] > num:
        #         stack.append((num,cur_idx))
        
        # return ans


        stack = []
        n = len(nums)
        ans = [-1]*len(nums)

        for i in range(2*n):

            num = nums[i%n]
            
            while stack and stack[-1][0] < num:
                ele,idx = stack.pop()
                ans[idx] = num
            
            if i<n:
                stack.append((num,i))
        
        return ans

