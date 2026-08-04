class Solution:
    def compress(self, chars: List[str]) -> int:
        '''
        Pattern - 2 pointer
        TC - O(N)
        SC - O(1)
        '''

        l = 0
        r = 0
        w = 0
        n = len(chars)

        while r<n:
            while r<n and chars[r] == chars[l]:
                r += 1
            
            
            chars[w] = chars[l]
            w+=1

            count = r - l
            if count > 1:
                for ch in str(count):
                    chars[w] = ch
                    w += 1
                    
            cnt = 0
            l = r
        
        return w
            