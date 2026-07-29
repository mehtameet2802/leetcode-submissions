class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        l_max = 0
        r_max = 0
        ans = 0

        while l <= r:
            if height[l] <= height[r]:
                l_max = max(l_max, height[l])
                ans += l_max - height[l]
                l+=1
            else:
                r_max = max(r_max, height[r])
                ans += r_max - height[r]
                r -= 1 
        
        return ans