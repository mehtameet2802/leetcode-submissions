class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = {}
        mp2 = {}

        if len(s)!=len(t):
            return False

        for st in s:
            if st not in mp:
                mp[st]=1
            else:
                mp[st] = mp[st]+1

        for st in t:
            if st not in mp2:
                mp2[st]=1
            else:
                mp2[st] = mp2[st]+1

        if len(mp)!=len(mp2):
            return False
        
        for item in mp:
            if item in mp2 and mp[item]==mp2[item]:
                continue
            else:
                return False
        
        return True