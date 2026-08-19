class NumberContainers:

    def __init__(self):
        self.index_map = {}
        self.number_heap = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.index_map[index] = number
        heapq.heappush(self.number_heap[number],index)

    def find(self, number: int) -> int:
        

        min_heap = self.number_heap[number]

        while min_heap:
            idx = min_heap[0]

            if idx not in self.index_map:
                return -1

            if self.index_map[idx] == number:
                return idx
            
            heapq.heappop(self.number_heap[number])
        
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)