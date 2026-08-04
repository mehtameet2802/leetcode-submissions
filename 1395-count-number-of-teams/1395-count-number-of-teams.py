class Solution:
    def numTeams(self, rating: List[int]) -> int:

        '''
        Patter - Fix Middle + Counting

        TC - O(N^2)
        SC - O(1)
        '''

        ans = 0
        n = len(rating)

        for j in range(n):

            ele = rating[j]

            leftSmaller = leftGreater = 0
            rightSmaller = rightGreater = 0

            for i in range(j):
                if rating[i] < ele:
                    leftSmaller += 1
                else:
                    leftGreater += 1
            
            for i in range(j+1,n):
                if rating[i] < ele:
                    rightSmaller += 1
                else:
                    rightGreater += 1

            ans += (leftSmaller * rightGreater)
            ans += (leftGreater * rightSmaller)
        
        return ans