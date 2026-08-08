class Solution:
    def minInsertions(self, s: str) -> int:
        right = 0
        ans = 0

        for ch in s:
            if ch == '(':

                if right % 2 == 1:
                    ans += 1
                    right -= 1

                right += 2

            else:
                right -= 1

                if right < 0:
                    ans += 1
                    right = 1

        return ans + right 