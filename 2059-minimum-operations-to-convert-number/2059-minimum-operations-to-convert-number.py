class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        '''
        N - len(nums)
        TC - O(N*1000)
        SC - O(1000)
        '''

        queue = deque([(start,0)])
        visited = {start}
        
        while queue:
            val, cnt = queue.popleft()

            if val == goal:
                return cnt

            if val>1000 or val<0:
                continue

            for num in nums:

                val1 = val + num
                val2 = val - num
                val3 = val ^ num

                if val1 not in visited:
                    queue.append((val1, cnt + 1))
                    visited.add(val1)
                
                if val2 not in visited:
                    queue.append((val2, cnt + 1))
                    visited.add(val2)
                
                if val3 not in visited:
                    queue.append((val3, cnt + 1))
                    visited.add(val3)
        
        return -1

            
