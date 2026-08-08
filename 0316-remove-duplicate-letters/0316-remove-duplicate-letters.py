class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # stack = []

        # def insert(a):
            
        #     if stack and stack[-1] == a:
        #         return
        #     elif stack and stack[-1] > a:
        #         ele = stack.pop()
        #         insert(a)
        #         stack.append(ele)
        #     else:
        #         stack.append(a)


        # for ch in s:
        #     insert(ch)
        
        # return "".join(stack)

        stack = []
        freq = Counter(s)
        seen = set()

        for ch in s:
            freq[ch] -= 1

            if ch in seen:
                continue
            
            while stack and stack[-1]>ch and freq[stack[-1]]>0:
                ele = stack.pop()
                seen.remove(ele)
            
            stack.append(ch)
            seen.add(ch)

        return "".join(stack)