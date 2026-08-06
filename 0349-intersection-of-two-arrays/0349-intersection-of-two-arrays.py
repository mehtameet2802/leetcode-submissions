class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
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
        #         if p1 > 0 and nums1[p1] == nums1[p1-1]:
        #             p1 += 1
        #             p2 += 1
        #             continue
                    
        #         ans.append(nums1[p1])
        #         p1 += 1
        #         p2 += 1
        #     elif nums1[p1] < nums2[p2]:
        #         p1 += 1
        #     else:
        #         p2 += 1
        
        # return ans

        '''
        Pattern - Hashset

        TC - O(N)
        SC - O(N)
        '''

        seen = set()

        ans = set()

        for num in nums1:
            seen.add(num)
        
        for num in nums2:
            if num in seen:
                ans.add(num)
        
        return list(ans)

