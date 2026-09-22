class Solution:
    def minSwaps(self, s: str) -> int:
        opening = 0
        closing = 0
        swaps = 0
        n = len(s)

        for ch in s:
            if ch == '[':
                if opening < n // 2:
                    opening += 1
                else:
                    closing += 1
                    swaps += 1
            else:
                if opening > closing:
                    closing += 1
                else:
                    opening += 1
                    swaps += 1
        
        return swaps // 2

