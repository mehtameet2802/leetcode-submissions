class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        '''
        DIrectly started coding and stuck in middle to actually find the splution, went to excalidraw and figured out the solution 
        the tc is of O(n*p)
        sc - O(p)
        getting TLE

        30 min spent

        still no optimized solution found

        Spent more 15 min and added a new while loop but now the problem is that hte negative numbers divisible by k are not being considered

        Then referred gpt and got that if remainder of 2 numbers is same then their diff is divisble by the number used to calculate ites remainder

        Time - 1 hr
        '''


        remainder_dict = defaultdict(int)
        remainder_dict[0] = 1

        prefix_sum = 0

        subarray_cnt = 0

        for cur_ele in nums:
            prefix_sum += cur_ele

            remainder = prefix_sum % k
            subarray_cnt += remainder_dict[remainder]

            remainder_dict[remainder] += 1
            
        return subarray_cnt
