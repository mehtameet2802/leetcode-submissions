class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        '''
        Pattern - Prefix Sum + Binary Search

        Preprocessing
        TC - O(N)
        SC - O(N)

        Each Query
        TC - O(log C)

        Overall
        TC - O(N + Q log C)
        SC - O(N)
        '''
        
        candles_index = []
        prefix_sum = [0]*len(s)

        for i,ch in enumerate(s):
            if ch == '|':
                candles_index.append(i)
        
        cur = 0
        for i,ch in enumerate(s):
            if ch == '*':
                cur += 1
            prefix_sum[i] = cur
        
        ans = []
        for start, end in queries:
            l = bisect_left(candles_index, start)
            r = bisect_right(candles_index, end) - 1

            if l > r or l == len(candles_index):
                ans.append(0)
            else:
                left_candle = candles_index[l]
                right_candle = candles_index[r]
                ans.append(prefix_sum[right_candle] - prefix_sum[left_candle])

        return ans