class StockPrice:

    def __init__(self):
        self.price_map = {}
        self.max_heap = [] 
        self.min_heap = [] 
        self.latest_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        self.latest_timestamp = max(self.latest_timestamp, timestamp)

        self.price_map[timestamp] = price

        heapq.heappush(self.max_heap,(-price,timestamp))
        heapq.heappush(self.min_heap,(price,timestamp))

    def current(self) -> int:
        return self.price_map[self.latest_timestamp]

    def maximum(self) -> int:
        while self.max_heap:
            price, time = self.max_heap[0]
            if self.price_map[time] == -price:
                return -price
            
            heapq.heappop(self.max_heap)

    def minimum(self) -> int:
        while self.min_heap:
            price, time = self.min_heap[0]
            if self.price_map[time] == price:
                return price
            
            heapq.heappop(self.min_heap)


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()