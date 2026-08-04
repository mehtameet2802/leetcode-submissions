class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}

        for i, num in enumerate(sorted(set(arr)),1):
            rank[num] = i

        for i, num in enumerate(arr):
            arr[i] = rank[arr[i]]
        
        return arr