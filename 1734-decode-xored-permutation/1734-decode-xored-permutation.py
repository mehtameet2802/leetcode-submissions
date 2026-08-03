class Solution:
    def decode(self, encoded: List[int]) -> List[int]:

        '''
        Pattern - Prefix XOR

        TC - O(N+1)
        SC - O(1)
        '''

        n = len(encoded) + 1

        total = 0
        for i in range(1,n+1):
            total = total^i

        odd = 0
        for i in range(1,n-1,2):
            odd = odd ^ encoded[i]
        
        first = total ^ odd
        ans = [first]
        cur = first

        for i in range(n-1):
            cur = encoded[i] ^ ans[i]
            ans.append(cur)
        
        return ans