class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        left = [0]*len(arr)
        right = [0]*len(arr)

        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            if stack:
                left[i] = i - stack[-1]
            else:
                left[i] = i+1
            
            stack.append(i)
        
        stack = []

        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack:
                right[i] = stack[-1] - i
            else:
                right[i] = len(arr) - i
            
            stack.append(i)
        
        contribution = 0
        for i in range(len(arr)):
            contribution += arr[i] * left[i] * right[i]

        return contribution % (pow(10,9) + 7)