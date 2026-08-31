class MyCalendar:

    '''
    Pattern - Binary Search

    TC - O(n + log n)
    SC - O(n)
    '''

    def __init__(self):
        self.arr = []

    def book(self, startTime: int, endTime: int) -> bool:
        if len(self.arr) < 1:
            self.arr.append((startTime,endTime))
            return True
        
        l = 0
        r = len(self.arr)-1

        while l<=r:
            mid = l + (r-l)//2

            if self.arr[mid][0] > startTime:
                r = mid - 1
            elif self.arr[mid][0] < startTime:
                l = mid + 1
            else:
                return False
            
        
        if l>0 and self.arr[l-1][1] > startTime:
            return False
        
        if l<len(self.arr) and self.arr[l][0] < endTime:
            return False
           
        self.arr.insert(l, (startTime,endTime))
        
        return True
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)