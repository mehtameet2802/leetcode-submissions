class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # '''
        # Pattern - Sort + Scan

        # TC - O(N log N)
        # SC - O(K)
        # '''

        # nums1.sort()
        # nums2.sort()

        # ans = []
        # p1 = p2 = 0

        # while p1<len(nums1) and p2<len(nums2):
        #     if nums1[p1] == nums2[p2]:                   
        #         ans.append(nums1[p1])
        #         p1 += 1
        #         p2 += 1
        #     elif nums1[p1] < nums2[p2]:
        #         p1 += 1
        #     else:
        #         p2 += 1
        
        # return ans

        '''
        Pattern - Sort + Scan

        TC - O(N log N)
        SC - O(K)
        '''

        f_map = defaultdict(int)
        
        for num in nums1:
            f_map[num] += 1        
        
        ans = []
        for num in nums2:
            if f_map[num] > 0:
                f_map[num] -= 1
                ans.append(num)
                
        return ans