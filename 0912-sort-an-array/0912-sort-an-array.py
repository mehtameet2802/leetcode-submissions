class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # '''
        # Pattern - Merge Sort

        # TC - O(n log n)
        # SC - O(n log n)
        # '''
        
        # def merge(left,right):
        #     ans = []
        #     l = 0
        #     r = 0

        #     while l<len(left) and r<len(right):
        #         if left[l] <= right[r]:
        #             ans.append(left[l])
        #             l += 1
        #         else:
        #             ans.append(right[r])
        #             r += 1
            
        #     while l<len(left):
        #         ans.append(left[l])
        #         l += 1
            
        #     while r<len(right):
        #         ans.append(right[r])
        #         r += 1

        #     return ans
        
        # def mergeSort(arr):

        #     if len(arr) <= 1:
        #         return arr
            
        #     mid = len(arr)//2

        #     left = mergeSort(arr[:mid])
        #     right = mergeSort(arr[mid:])

        #     return merge(left,right)

        # return mergeSort(nums)


        '''
        Pattern - Merge Sort

        TC - O(n log n)
        SC - O(n)
        '''
        
        def merge(left,mid,right):
            temp = []
            
            i = left
            j = mid + 1

            while i<=mid and j<=right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            
            while i<=mid:
                temp.append(nums[i])
                i += 1
            
            while j<=right:
                temp.append(nums[j])
                j += 1

            nums[left:right+1] = temp
        
        def mergeSort(left, right):

            if left >= right:
                return
            
            mid = (right + left)//2

            mergeSort(left,mid)
            mergeSort(mid+1,right)

            merge(left,mid,right)

        mergeSort(0, len(nums)-1)
        return nums