class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = []

        for i,temp in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                temperatures[j] = i-j
            
            stack.append(i)

        while stack:
            temperatures[stack.pop()] = 0

        return temperatures