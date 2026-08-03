class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        arr = [0]*101

        for log in logs:
            arr[log[0]-1950] += 1
            arr[log[1]-1950] -= 1
        
        ans = 0
        cur = 0
        max_p = 0
        for i in range(101):
            cur += arr[i]
            if cur > max_p:
                max_p = cur
                ans = i
        
        return ans+1950