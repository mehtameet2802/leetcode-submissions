class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # '''
        # Pattern - Fixed Sliding Window

        # TC - O(N)
        # SC - O(1)
        # '''

        # normal_total = 0
        # for i in range(len(grumpy)):            
        #     if grumpy[i] == 0:
        #         normal_total += customers[i]

        # window = minutes
        # left = 0
        # ans = 0
        # cur = 0
        # grumpy_window_total = 0

        # for right in range(len(grumpy)):
        #     cur += customers[right]

        #     if grumpy[right] == 0:
        #         grumpy_window_total += customers[right]

        #     if right - left + 1 == window:
        #         ans = max(ans, cur + normal_total - grumpy_window_total)
        #         cur -= customers[left]

        #         if grumpy[left] == 0:
        #             grumpy_window_total -= customers[left]

        #         left += 1          

        # return ans


        '''
        Pattern - Fixed Sliding Window

        TC - O(N)
        SC - O(1)
        '''

        normal_total = 0
        for i in range(len(grumpy)):            
            if grumpy[i] == 0:
                normal_total += customers[i]

        window = minutes
        left = 0
        ans = 0
        extra_gain = 0

        for right in range(len(grumpy)):
            
            if grumpy[right] == 1:
                extra_gain += customers[right]

            if right - left + 1 == window:
                ans = max(ans, extra_gain + normal_total)
                
                if grumpy[left] == 1:
                    extra_gain -= customers[left]

                left += 1          

        return ans