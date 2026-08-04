class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        r = 0
        w = 0
        n = len(chars)


        cnt = 0
        ans = []

        while r<n:
            while r<n and chars[r] == chars[l]:
                r += 1
                cnt += 1
            
            count = str(cnt)
            chars[w] = chars[l]
            w+=1
            if cnt > 1:
                for ch in count:
                    chars[w] = ch
                    w += 1
            cnt = 0
            l = r
        
        return w
            