class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        # '''
        # Pattern - Prefix and Suffix Count and Sum

        # TC - O(N)
        # SC - O(N)
        # '''

        # n = len(boxes)
        # pre = [[0,0] for _ in range(n)]
        # suf = [0,0]

        # for i in range(1,n):
        #     prev = pre[i-1]
        #     new = [prev[0]+prev[1], prev[1]]
        #     if boxes[i-1] == '1':
        #         new = [new[0]+1, new[1]+1]
        #     pre[i] = new
                
        # ans = []
        # for i in range(n-1,-1,-1):
        #     ans.append(pre[i][0] + suf[0])
        #     new = [suf[0]+suf[1], suf[1]]

        #     if boxes[i] == '1':
        #         suf = [new[0]+1,new[1]+1]
        #     else:
        #         suf = new
        
        # return ans[::-1]

        '''
        Pattern - Prefix and Suffix Count and Sum

        TC - O(N)
        SC - O(1)
        '''

        n = len(boxes)
        ans = [0] * n
        suf = 0

        moves = 0
        balls = 0

        for i in range(n):

            ans[i] = moves

            if boxes[i] == '1':
                balls += 1

            moves += balls
        
        moves = 0
        balls = 0

        for i in range(n-1,-1,-1):
            ans[i] += moves

            if boxes[i] == '1':
                balls += 1
            
            moves += balls
        
        return ans