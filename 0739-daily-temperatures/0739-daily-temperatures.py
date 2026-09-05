class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for cur_idx,cur_temp in enumerate(temperatures):
            if not stack:
                stack.append((cur_temp,cur_idx))
                continue
            
            while stack and stack[-1][0] < cur_temp:
                temp, idx = stack.pop()
                ans[idx] = cur_idx - idx
            
            stack.append((cur_temp, cur_idx))
        
        return ans
