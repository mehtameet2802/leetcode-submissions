class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        '''
        Pattern - FIxed Window

        TC - O(N)
        SC - O(1)
        '''

        number = str(num)

        left = 0
        ans = 0
        cur = 0
        power = pow(10,k-1)

        for right in range(len(number)):
            cur = cur*10 + int(number[right])

            if right - left + 1 == k:
                if cur > 0 and num % cur == 0:
                    ans += 1
                
                cur -= (int(number[left]) * power)
                left += 1
        return ans