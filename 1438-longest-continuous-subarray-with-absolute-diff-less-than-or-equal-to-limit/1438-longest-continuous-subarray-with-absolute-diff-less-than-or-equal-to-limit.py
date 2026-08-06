class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        '''
        Pattern - Sliding Window + Deque

        TC - O(N)
        SC - O(N)
        '''
        
        left = 0
        ans = 0

        max_queue = deque([])
        min_queue = deque([])

        for right in range(len(nums)):

            while max_queue and nums[max_queue[-1]] < nums[right]:
                max_queue.pop()
            
            max_queue.append(right)

            while min_queue and nums[min_queue[-1]] > nums[right]:
                min_queue.pop()
            
            min_queue.append(right)

            while abs(nums[max_queue[0]] - nums[min_queue[0]]) > limit:
                
                if max_queue[0] == left:
                    max_queue.popleft()
                
                if min_queue[0] == left:
                    min_queue.popleft()

                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans

