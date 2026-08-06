class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # '''
        # Pattern - HashSet + Custom Sort

        # U - number of unique N

        # TC - O(N + U log U)
        # SC - O(U)
        # '''

        # ans = []

        # f_map = Counter(arr1)

        # for num in arr2:
        #     while f_map[num] > 0:
        #         ans.append(num)
        #         f_map[num] -= 1
            
        #     del f_map[num]
        
        # for num in sorted(f_map.keys()):
        #     while f_map[num] > 0:
        #         ans.append(num)
        #         f_map[num] -= 1
            
        #     del f_map[num]
        
        # return ans
        
        '''
        Pattern - HashSet + Custom Sort

        U - number of unique N

        TC - O(N)
        SC - O(1)
        '''

        ans = []
        f_arr = [0]*1001

        for num in arr1:
            f_arr[num] += 1

        for num in arr2:
            ans.extend([num] * f_arr[num])
            f_arr[num] = 0
        
        for i, num in enumerate(f_arr):
            ans.extend([i]*num)

        return ans
        
