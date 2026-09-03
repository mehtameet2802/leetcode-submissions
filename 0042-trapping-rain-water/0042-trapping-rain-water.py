class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        left pointer on left start
        right pointer on right start
        the pointer wiht lower height moves forward
        at each index, it is checked if left is smaller or right is smaller
        at each array index max of left and max of right is calculated
        water is added which is max of current min - current min
        return ans
        '''

        left = 0
        right = len(height) - 1
        max_l = 0
        max_r = 0
        ans = 0

        while left < right:
            if height[left] < height[right]:
                max_l = max(height[left], max_l)
                ans += max_l - height[left]
                left += 1
            else:
                max_r = max(height[right], max_r)
                ans += max_r - height[right]
                right -= 1
        
        return ans
            
