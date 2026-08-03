class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        arr = [0] * 52

        for s,e in ranges:
            arr[s] += 1
            arr[e+1] -= 1

        cover = 0
        for i in range(52):
            cover += arr[i]

            if left<=i<=right and cover <= 0:
                return False
        
        return True

