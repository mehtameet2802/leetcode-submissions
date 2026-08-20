class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.double = []

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.booked and not self.double:
            self.booked.append([startTime,endTime])
            return True
        
        for a,b in self.double:
            if (startTime < b and startTime >= a) or (a >= startTime and a < endTime):
                return False

        for a,b in self.booked:
            if (startTime < b and startTime >= a) or (a >= startTime and a < endTime):
                self.double.append(
                    [
                        max(startTime,a),
                        min(endTime,b)
                    ]
                )
        

        self.booked.append(
            [startTime,endTime]
        )
        
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)