class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        idx_map = {}

        for i,num in enumerate(nums2):
            idx_map[num] = i

            while stack and nums2[stack[-1]] < num:
                j = stack.pop()
                nums2[j] = num
            
            stack.append(i)
        

        for i, num in enumerate(nums1):
            if nums2[idx_map[num]] == num:
                nums1[i] = -1
            else:
                nums1[i] = nums2[idx_map[num]]
        
        return nums1
        