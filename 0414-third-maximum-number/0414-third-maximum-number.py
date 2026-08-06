class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # '''
        # Pattern - Sort + Scan

        # TC - O(N log N)
        # SC - O(1)
        # '''

        # n = len(nums)
        # if n<3:
        #     return max(nums)
        
        # nums.sort()

        # cnt = 0
        # for i in range(n-1,-1,-1):
        #     if i<n-1 and nums[i] == nums[i+1]:
        #         continue
        #     cnt += 1
        #     if cnt == 3:
        #         return nums[i]
            
        # if cnt < 3:
        #     return nums[-1]

        '''
        Pattern - Top KTracking

        TC - O(N)
        SC - O(1)
        '''

        first = second = third = None

        for num in nums:

            if num == first or num == second or num == third:
                continue
            
            if first == None or num > first:
                third = second
                second = first
                first = num
            
            elif second == None or num > second:
                third = second
                second = num
            
            elif third == None or num > third:
                third = num
            
        
        return first if third == None else third
