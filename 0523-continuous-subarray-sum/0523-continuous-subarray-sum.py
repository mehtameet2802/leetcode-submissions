class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        Pattern prediction: divisble values are part of same remainder bucket
        What does prefix_sum represent? - running sum of all elements upto a particular index
        What does a repeated remainder prove? - a repeated remainder means sum of arrays until those index are divsible by k
        What must the dictionary store: earliest index or frequency? - it should store the earliest index of the remainder, using which we can check the length >= 2
        Why is the length condition needed? - good subarray says min length 2 
        
        Invariant:
        all the numbers in the iteration are valid, only return true when the good suaarray condition is satisfied, outside for lop return false
        
        Pseudocode:
        maintain a var prefix_sum
        maintain a remainders dict for remainder : first_index
        add remainders[0] = -1, for consider subarray starting from 0
        using for loop incrementally calculate prefix sum
        for each preifx sum do mod and get remainder
        if remainder already in the remainders dict, then calculate the diff of cur_index and remainder first_index, to check if length >= 2
        if yes then return true
        outside for loop return false

        Complexity: TC - O(n) SC - O(n)
        '''

        remainders = {}
        remainders[0] = -1
        prefix_sum = 0

        for idx, num in enumerate(nums):
            prefix_sum += num

            remainder = prefix_sum % k
            if remainder in remainders:
                if idx - remainders[remainder] >= 2:
                    return True
            else:
                remainders[remainder] = idx
        
        return False
