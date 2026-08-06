class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []

        f_map = Counter(arr1)

        for num in arr2:
            while f_map[num] > 0:
                ans.append(num)
                f_map[num] -= 1
            
            del f_map[num]
        
        for num in sorted(f_map.keys()):
            while f_map[num] > 0:
                ans.append(num)
                f_map[num] -= 1
            
            del f_map[num]
        
        return ans
        
