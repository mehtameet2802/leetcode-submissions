class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        # '''
        # Pattern - Fixed Sliding Window

        # TC - O(N)
        # SC - O(1)
        # '''

        # left = 0
        # total = 0
        # ans = 0

        # for right in range(len(arr)):
        #     total += arr[right]

        #     if right - left + 1 == k:
        #         avg = total / k

        #         if avg >= threshold:
        #             ans += 1
                
        #         total -= arr[left]
        #         left += 1
        
        # return ans

        '''
        Pattern - Fixed Sliding Window

        TC - O(N)
        SC - O(1)
        '''

        left = 0
        total = 0
        ans = 0
        target = threshold * k 

        for right in range(len(arr)):
            total += arr[right]

            if right - left + 1 == k:
                
                if total >= target:
                    ans += 1
                
                total -= arr[left]
                left += 1
        
        return ans