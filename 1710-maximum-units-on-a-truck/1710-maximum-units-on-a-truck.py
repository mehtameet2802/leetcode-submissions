class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        arr = []

        for item in boxTypes:
            arr.extend([item[1]]*item[0])
        
        arr.sort()

        l = 0
        r = len(arr) - 1

        # print(arr)

        ans = 0
        while r>=0 and truckSize>0:
            ans += arr[r]
            truckSize -= 1
            r -= 1
        
        return ans

51