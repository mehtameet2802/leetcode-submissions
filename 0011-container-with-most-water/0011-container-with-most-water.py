class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        1. What is the required output? - max area
        2. Which constraints eliminate brute force? - we take 2 pointers and the pointer with lower height is moved inwards, until 2 pointers cross each other
        3. Draw one normal and one dangerous example.
        4. State the brute-force approach. - we do 2 for loop and check all pairs of indexes to determine the max area
        5. State what each variable/data structure represents. - left is the array elements from left side, right is array elements from right, area is the max area, cur_area is the area for cur combination of left and right 
        6. Write the invariant. 
        7. Fix the loop boundaries. left < right
        8. Dry-run one iteration.


        The question is seen multiple times and solved multiples time hence in memor, but ufcourse used excalidraw and wrote above answers

        TC - O(n)
        SC - O(1)
        '''

        left = 0
        right = len(height) - 1
        area = 0

        while left < right:
            width = right - left
            if height[left] < height[right]:
                cur_area = height[left] * width
                left += 1
            else:
                cur_area = height[right] * width 
                right -= 1
            
            area = max(area, cur_area)
        
        return area
                

