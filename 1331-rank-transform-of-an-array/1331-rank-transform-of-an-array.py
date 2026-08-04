class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        '''
        TC - O(U log U)
        SC - O(U) - Unique elements
        '''

        rank = {}

        for i, num in enumerate(sorted(set(arr)),1):
            rank[num] = i

        for i, num in enumerate(arr):
            arr[i] = rank[num]
        
        return arr