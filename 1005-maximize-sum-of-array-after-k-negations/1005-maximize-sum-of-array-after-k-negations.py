class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        neg = []
        pos = []

        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        neg.sort()
        
        
        i = 0
        while k>0 and i<len(neg):
            neg[i] = -1*neg[i]
            i += 1
            k -= 1

        if k>0:
            pos.extend(neg)
            pos.sort()
            k = k%2
            
            if k:
                pos[0] = -1*pos[0]

            return sum(pos)
        
        return sum(neg) + sum(pos)