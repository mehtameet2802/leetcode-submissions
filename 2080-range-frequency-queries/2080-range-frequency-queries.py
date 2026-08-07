class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.pos = defaultdict(list)

        for i,num in enumerate(arr):
            self.pos[num].append(i)

    def query(self, left: int, right: int, value: int) -> int:

        if value not in self.pos:
            return 0

        arr = self.pos[value]

        l = bisect_left(arr, left)
        r = bisect_right(arr, right)

        return r - l


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)