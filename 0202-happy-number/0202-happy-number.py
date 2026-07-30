class Solution:
    def isHappy(self, n: int) -> bool:

        # '''
        # TC - O(n*len(n))
        # SC - O(n)
        # '''

        # seen = set()

        # def cal(num):
        #     new_num = 0
        #     while num>0:
        #         new_num += pow(num%10,2)
        #         num = num//10
        #     return new_num


        # while n not in seen:
        #     seen.add(n)
        #     if n == 1:
        #         return True
        #     n = cal(n)
            
        
        # return False


        '''
        Pattern - FLoyd Cycle Detection

        TC - O(log n)
        SC - O(1)
        '''


        def cal(num):
            new_num = 0
            while num>0:
                new_num += pow(num%10,2)
                num = num//10
            return new_num

        slow = n
        fast = cal(n)

        while fast!=1 and slow!=fast:
            fast = cal(cal(fast))
            slow = cal(slow)

        
        return fast == 1