class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # stack = []
        # idx_map = {}

        # for i,num in enumerate(nums2):
        #     idx_map[num] = i

        #     while stack and nums2[stack[-1]] < num:
        #         j = stack.pop()
        #         nums2[j] = num
            
        #     stack.append(i)
        

        # for i, num in enumerate(nums1):
        #     if nums2[idx_map[num]] == num:
        #         nums1[i] = -1
        #     else:
        #         nums1[i] = nums2[idx_map[num]]
        
        # return nums1
        

        stack = []
        greater = {}

        for num in nums2:

            while stack and stack[-1] < num:
                greater[stack.pop()] = num
            
            stack.append(num)
        
        while stack:
            greater[stack.pop()] = -1

        for i, num in enumerate(nums1):
            nums1[i] = greater[num]
        
        return nums1