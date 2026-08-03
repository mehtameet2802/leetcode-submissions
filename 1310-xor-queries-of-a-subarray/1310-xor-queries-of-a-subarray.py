class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        pre_xor = [0]*len(arr)

        

        for i, ele in enumerate(arr):
            if i == 0:
                pre_xor[0] = arr[0]
                continue
            pre_xor[i] = ele^pre_xor[i-1]
        
        for i,j in queries:
            if i == 0:
                ans.append(pre_xor[j])
                continue
            ans.append(pre_xor[j]^pre_xor[i-1])
        
        return ans