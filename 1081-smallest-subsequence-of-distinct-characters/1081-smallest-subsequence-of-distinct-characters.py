class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        seen = set()
        freq = Counter(s)

        for ch in s:
            freq[ch] -= 1

            if ch in seen:
                continue

            while stack and stack[-1] > ch and freq[stack[-1]] > 0:
                ele = stack.pop()
                seen.remove(ele)
            
            seen.add(ch)
            stack.append(ch)
        
        return "".join(stack)