class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        min_heap = []



        for i, num in enumerate(nums1):
            heapq.heappush(min_heap,(nums1[i]+nums2[0],i,0))
        
        ans = []

        while k>0:
            sum_val, num1_idx, num2_idx = heapq.heappop(min_heap)
            ans.append([nums1[num1_idx], nums2[num2_idx]])

            new_num2_idx = num2_idx + 1
            if new_num2_idx < len(nums2):
                heapq.heappush(min_heap, (nums1[num1_idx]+nums2[new_num2_idx], num1_idx, new_num2_idx))
            
            k-=1
        
        return ans