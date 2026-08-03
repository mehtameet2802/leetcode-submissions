from collections import Counter

class Solution:
    def numSplits(self, s: str) -> int:

        # '''
        # Pattern - Prefix + Suffix (Distinct Count)

        # TC - O(N)
        # SC - O(N)
        # '''

        # splits = 0
        # seen = set()

        # n = len(s)

        # pre = [0]*n
        # suf = [0]*n

        # for i in range(n):
        #     seen.add(s[i])
        #     pre[i] = len(seen)

        # seen.clear()
        # for i in range(n-1,-1,-1):
        #     seen.add(s[i])
        #     suf[i] = len(seen)
        
        # for i in range(n-1):
        #     if pre[i] == suf[i+1]:
        #         splits += 1
        
        # return splits


        '''
        Pattern - Prefix + Suffix (Distinct Count)

        TC - O(N)
        SC - O(U), u is unique characters
        '''

        splits = 0

        n = len(s)

        left = set()
        right = Counter(s)

        for i in range(n-1):
            left.add(s[i])
            right[s[i]] -= 1

            if right[s[i]] <= 0:
                del right[s[i]]
            
            if len(left) == len(right):
                splits += 1
        
        return splits