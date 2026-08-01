class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        # '''
        # Pattern - 

        # TC - O(n)
        # SC - O(1)
        # '''

        # f_arr = [[0,0] for _ in range(1001)]

        # o_map = defaultdict(int)

        # for num in arr:
        #     if num < 0:
        #         f_arr[-num][1] += 1
        #     else:
        #         f_arr[num][0] += 1
        
        # for a,b in f_arr:            
        #     if a>0:
        #         o_map[a] += 1
            
        #     if b>0:
        #         o_map[b] += 1
            
        #     if o_map[a]>1 or o_map[b]>1:
        #         return False
        
        # return True


        '''
        Pattern - 

        TC - O(n)
        SC - O(1)
        '''

        f_arr = [[0,0] for _ in range(1001)]

        o_set = set()

        for num in arr:
            if num < 0:
                f_arr[-num][1] += 1
            else:
                f_arr[num][0] += 1
        
        for a,b in f_arr:            
            if a>0:
                if a in o_set:
                    return False
                o_set.add(a)
            
            if b>0:
                if b in o_set:
                    return False
                o_set.add(b)
                    
        return True
        

