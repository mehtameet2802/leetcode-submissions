class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        min_heap = []
        max_heap = []

        def balance():
            if abs(len(min_heap)-len(max_heap)) > 1:
                if len(min_heap) > len(max_heap):
                    heapq.heappush(max_heap, -heapq.heappop(min_heap))
                else:
                    heapq.heappush(min_heap, -heapq.heappop(max_heap))


        def push(nums):
            for num in nums:
                if not max_heap:
                    heapq.heappush(max_heap, -num)
                elif -max_heap[0] >= num:
                    heapq.heappush(max_heap, -num)
                else:
                    heapq.heappush(min_heap, num)
                
                balance()

        push(nums1)
        push(nums2)
        
        if len(min_heap) == len(max_heap):
            return (min_heap[0] - max_heap[0])/2
        elif len(min_heap) > len(max_heap):
            return min_heap[0]
        else:
            return -max_heap[0]