class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        '''
        Pattern - QuickSelect
        TC - O(n), worst O(n^2)
        SC - O(1) - this is iterative, if recursive then worst - O(n), avg O(log n)
        '''
        
        def distance(arr):
            a = arr[0]
            b = arr[1]
            return pow(a,2)+pow(b,2)

        def partition(left, right):
            i = left
            pivot = distance(points[right])

            for j in range(left,right):
                if distance(points[j]) <= pivot:
                    points[i], points[j] = points[j], points[i]
                    i+=1
            
            points[i], points[right] = points[right], points[i]

            return i
        
        def quickSelect(left, right):

            pivot = partition(left, right)

            if pivot == k - 1:
                pivot
            elif pivot < k - 1:
                quickSelect(pivot + 1, right)
            else:
                quickSelect(left, pivot - 1)
        
        quickSelect(0,len(points)-1)

        return points[:k]

