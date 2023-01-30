class Solution:
    def reverseWords(self, s: str) -> str:
        j = s.split(" ")
        ans = ""
        for i in range(len(j)):
            if i != len(j)-1:
                ans = ans+j[i][::-1]+" "
            else:
                ans = ans+j[i][::-1]
        return ans