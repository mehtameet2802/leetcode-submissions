class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda x : x[1])
        r = len(boxTypes) - 1

        ans = 0
        while r>=0 and truckSize>0:

            if truckSize >= boxTypes[r][0]: 
                ans += boxTypes[r][0] * boxTypes[r][1]
                truckSize -= boxTypes[r][0]
            else:
                ans += boxTypes[r][1] * truckSize
                truckSize = 0
            r -= 1
        
        return ans

51