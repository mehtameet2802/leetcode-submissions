class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = []

        for idx,num1 in enumerate(nums1):
            heapq.heappush(min_heap,(num1+nums2[0],idx,0))
        
        ans = []

        while len(ans)!=k:
            ele_sum, num1_idx, num2_idx = heapq.heappop(min_heap)

            num1 = nums1[num1_idx]
            num2 = nums2[num2_idx]

            ans.append([nums1[num1_idx],nums2[num2_idx]])

            num2_idx += 1

            if num2_idx < len(nums2):
                heapq.heappush(min_heap, (num1+nums2[num2_idx],num1_idx,num2_idx))
        
        return ans