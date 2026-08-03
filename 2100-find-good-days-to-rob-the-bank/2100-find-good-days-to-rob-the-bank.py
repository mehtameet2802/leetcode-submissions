class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:

        # '''
        # Pattern - Prefix + Suffix Count
        
        # TC - O(N)
        # SC - O(N)
        # '''

        # pre = 0
        # suf = 0
        # n = len(security)

        # pre_days = [0]*n
        # suf_days = [0]*n

        # for i in range(n-1):
        #     pre_days[i] = pre
        #     if security[i] >= security[i+1]:
        #         pre += 1
        #     else:
        #         pre = 0
        
        # pre_days[n-1] = pre
    

        # for i in range(n-1,0,-1):
        #     suf_days[i] = suf
        #     if security[i] >= security[i-1]:
        #         suf += 1
        #     else:
        #         suf = 0
        
        # suf_days[0] = suf

        # ans = []
        # for i in range(n):
        #     if pre_days[i] - time >= 0 and suf_days[i] - time >= 0:
        #         ans.append(i)
        
        # return ans


        '''
        Pattern - Prefix + Suffix Count
        
        TC - O(N)
        SC - O(N)
        '''

        pre = 0
        suf = 0
        n = len(security)

        pre_days = [0]*n

        for i in range(n-1):
            pre_days[i] = pre
            if security[i] >= security[i+1]:
                pre += 1
            else:
                pre = 0
        
        pre_days[n-1] = pre
            
        
        ans = []
        for i in range(n-1,0,-1):
            if pre_days[i] >= time and suf >= time:
                ans.append(i)

            if security[i] >= security[i-1]:
                suf += 1
            else:
                suf = 0
        
        if pre_days[0] >= time and suf >= time:
            ans.append(0)

        
        return ans