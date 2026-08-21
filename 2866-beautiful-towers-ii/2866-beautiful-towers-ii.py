class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)

        left = [0]*n
        right = [0]*n

        stack = []

        for i in range(n):
            while stack and maxHeights[stack[-1]] > maxHeights[i]:
                stack.pop()
            
            if stack:
                j = stack[-1]

                left[i] = left[j] + maxHeights[i]*(i-j) 
            else:
                left[i] = maxHeights[i] * (i+1)
            
            stack.append(i)
        
        stack = []
        for i in range(n-1,-1,-1):
            while stack and maxHeights[stack[-1]] > maxHeights[i]:
                stack.pop()
            
            if stack:
                j = stack[-1]

                right[i] = right[j] + maxHeights[i]*(j-i)
            else:
                right[i] = maxHeights[i] * (n-i)

            stack.append(i)
        
        ans = 0
        for i in range(n):
            total = left[i] + right[i] - maxHeights[i]
            ans = max(ans,total)
        
        return ans