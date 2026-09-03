class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        I will create a set of all the elements

        Then iterate over the elements and for each element check if the 
        cur_ele-1 exist or not.

        if cur_ele-1 exist then continue
        else consider that the start point and start iterating by +1 until elemnts exist

        This will provide me the count of ans, and I will update the ans with max

        I could recollect this from memory as have solve it multiple times


        Wrote first solution without considered in 5 min and submitted passed 81 cases and got TLE, thought 7 mins more and added considered set along with its condition to prevent duplicate runs from same starb points

        TC - O(n) - because very less elements for which I will be able to iterate by +1 until n, most will break
        SC - O(n)
        '''

        seen = set(nums)
        considered = set()
        seq_len = 0

        for cur_ele in nums:
            if cur_ele - 1 in seen:
                continue
            
            if cur_ele in considered:
                continue

            considered.add(cur_ele)
            next_ele = cur_ele + 1
            cur_seq_len = 1
            while next_ele in seen:
                cur_seq_len += 1
                next_ele += 1
            
            seq_len = max(seq_len, cur_seq_len)

        return seq_len