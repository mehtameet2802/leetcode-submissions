class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        TC - O(n)
        SC: O(1) auxiliary, O(n) including the output array

        First drew the test case and tried solving the problme on excalidraw by iterating
        Found the solution but still during writing had to think a bit and go back and forth on ecalidraw during writing of suffix part (it seems I started writing code early)

        then wrote code and 1 test case failed, found that in prefix calculation had started from 2 instead of 1, had to draw some iteration of failed test case on excalidraw to identify the root cause and then resolved it, also had to use print statement to print prefix_mul
        

        Mistake:
        Started the prefix loop at index 2 instead of index 1.

        Root cause:
        Started coding before defining what each array position represented.

        Prevention rule:
        Before writing either loop, state:
        answer[i] initially stores the product strictly left of i;
        suffix_product stores the product strictly right of i.
        
        '''

        prefix_arr = [1]*len(nums)

        for idx in range(1,len(nums)):
            prefix_arr[idx] = prefix_arr[idx-1] * nums[idx-1]

        suffix_mul = nums[-1]

        for idx in range(len(nums)-2,-1,-1):
            prefix_arr[idx] = prefix_arr[idx] * suffix_mul
            suffix_mul = suffix_mul * nums[idx]
        
        return prefix_arr
