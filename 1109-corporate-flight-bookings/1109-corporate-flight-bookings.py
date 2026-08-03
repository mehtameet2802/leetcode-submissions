class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0]*(n+2)

        for ele in bookings:
            s = ele[0]
            e = ele[1]
            booking = ele[2]
            arr[s] += booking
            arr[e+1] -= booking
        
        cur = 0
        ans = []
        for i in range(1,n+1):
            cur += arr[i]
            ans.append(cur)
        
        return ans