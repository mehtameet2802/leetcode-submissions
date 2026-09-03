from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        TC - O(n)
        SC - O(n)


        Drew the test cases on the excalidraw
        when iterated throught testcase 1 - easily found that will require an array and dict, while writing the text realised only need dict to store freq of prefix sum

        when iterated through the testcase 2, found hidden condition of comapring current val in nums with k, if they match then ans_count increases by 1

        during iteration we subtract k from prefix sum, and check if the val is in dict, if exists then we add its freq to ans, as that is the number of times the sub array sum equal to k, from that i to cur num (j), creates sub array with sum as k

        if would have not checked the second test must have missed the comaprision of k == num in iteration

        dict will have default value 0 and a value 0 with freq 1 to represent array startign from 0

        '''

        prefix_sum = [0]*len(nums)
        freq_dict = defaultdict(int)
        freq_dict[0] = 1
        sub_arr_cnt = 0

        prefix_sum = 0

        for cur_ele in nums:

            prefix_sum += cur_ele

            diff = prefix_sum - k
            if diff in freq_dict:
                sub_arr_cnt += freq_dict[diff]

            freq_dict[prefix_sum] += 1
        
        return sub_arr_cnt
