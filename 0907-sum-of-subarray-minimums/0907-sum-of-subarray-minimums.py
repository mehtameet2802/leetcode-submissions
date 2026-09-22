class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        stack = []
        ans = 0

        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                ele_idx = stack.pop()
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                
                right = i

                left_span = ele_idx - left
                right_span = right - ele_idx
                ans += arr[ele_idx] * left_span * right_span
            
            stack.append(i)
        
        while stack:
            ele_idx = stack.pop()
            if stack:
                left = stack[-1]
            else:
                left = -1
            
            right = len(arr)
            left_span = ele_idx - left
            right_span = right - ele_idx
            ans += arr[ele_idx]*left_span*right_span
        
        return ans % (pow(10,9)+7)