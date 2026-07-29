class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """



        p1 = m-1
        p2 = n-1

        w = m+n-1

        while w>=0:
            if p1>=0 and p2>=0:
                if nums1[p1] >= nums2[p2]:
                    nums1[w] = nums1[p1]
                    p1-=1
                else:
                    nums1[w] = nums2[p2]
                    p2-=1
            else:
                if p1>=0:
                    nums1[w] = nums1[p1]
                    p1-=1
                elif p2>=0:
                    nums1[w] = nums2[p2]
                    p2-=1 

            w-=1