class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        pre = [[0,0] for _ in range(n)]
        suf = [[0,0] for _ in range(n)]

        for i in range(1,n):
            prev = pre[i-1]
            new = [prev[0]+prev[1], prev[1]]
            if boxes[i-1] == '1':
                new = [new[0]+1, new[1]+1]
            pre[i] = new
        
        for i in range(n-2,-1,-1):
            prev = suf[i+1]
            new = [prev[0]+prev[1], prev[1]]

            if boxes[i+1] == '1':
                new = [new[0]+1, new[1]+1]
            
            suf[i] = new
        
        ans = []
        for i in range(n):
            ans.append(pre[i][0] + suf[i][0])
        
        return ans