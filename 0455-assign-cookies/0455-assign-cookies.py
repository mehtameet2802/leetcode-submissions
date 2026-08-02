class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        # '''
        # Pattern - Greedy
        # TC - O(N^2)
        # SC - O(1)

        # '''

        # cnt = 0
        # g.sort(reverse=True)
        # s.sort()

        # for cookie in s:
        #     for i, child in enumerate(g):
        #         if child == -1:
        #             continue
        #         if cookie >= child:
        #             cnt += 1
        #             g[i] = -1
        #             break

        # return cnt 


        '''
        Pattern - Greedy + 2 Pointer
        TC - O(Nlog N + M log M)
        SC - O(1)

        '''

        g.sort()
        s.sort()

        child = 0 
        cookie = 0

        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                cookie += 1
                child += 1
            else:
                cookie += 1
            
        return child