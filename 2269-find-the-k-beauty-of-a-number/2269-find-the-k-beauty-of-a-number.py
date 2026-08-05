class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        number = str(num)

        left = 0
        ans = 0
        cur = 0

        for right in range(len(number)):
            cur = cur*10 + int(number[right])

            print(cur)
            if right - left + 1 == k:
                if cur > 0 and num % cur == 0:
                    ans += 1
                
                cur -= (int(number[left]) * pow(10,k-1))
                left += 1
        return ans