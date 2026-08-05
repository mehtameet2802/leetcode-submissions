class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        '''
        Pattern - DNF/3 Way Partioning-caanot be used as order has to be maintained,
        Use 3 arrays

        TC - O(N)
        SC - O(N)
        '''

        n = len(nums)
        L = []
        R = []
        mid = []

        for i in range(n):
            if nums[i] == pivot:
                mid.append(nums[i])
            elif nums[i] > pivot:
                R.append(nums[i])
            else:
                L.append(nums[i])
        
        return L + mid + R