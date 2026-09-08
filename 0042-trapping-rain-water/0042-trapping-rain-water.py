class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        What does max_left represent? - it represnets the max height boundary on the left
        What does max_right represent? - it represnets the max height boundary on the right
        Why is it safe to process the shorter boundary? - that is max height that the water can reach and be stored, beyond that overfill and spilling will happen and no storing
        What water amount is finalized at that pointer?, the width at each pointer is 1, so water amount is min(max_left, max_right) - height
        '''

        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0
        ans = 0

        while left <= right :
            if height[left] < height[right]:
                max_left = max(max_left, height[left])
                ans += max_left - height[left]
                left += 1
            else:
                max_right = max(max_right, height[right])
                ans += max_right - height[right]
                right -= 1

        return ans