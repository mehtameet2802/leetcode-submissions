class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''
        Pattern - Reverse Fixed Size Array

        TC - O(N)
        SC - O(1)
        '''

        left = 0
        window = len(cardPoints) - k
        total = sum(cardPoints) 
        ans = total
        cur = 0

        for right in range(len(cardPoints)):
            cur += cardPoints[right]

            if right - left + 1 == window:
                ans = min(ans, cur)

                cur -= cardPoints[left]
                left += 1
        
        if k == len(cardPoints):
            return ans
        return total - ans