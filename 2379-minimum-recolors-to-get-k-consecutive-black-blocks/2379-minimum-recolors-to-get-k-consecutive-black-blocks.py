class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        '''
        Pattern - Fixed Sliding Window
        TC - O(N)
        SC - O(1)
        '''

        left = 0
        ans = len(blocks)+1
        w_blocks = 0

        for right in range(len(blocks)):
            if blocks[right] == 'W':
                w_blocks += 1

            if right - left + 1 == k:
                ans = min(w_blocks, ans)
                
                if blocks[left] == 'W':
                    w_blocks -= 1

                left += 1

        return ans 