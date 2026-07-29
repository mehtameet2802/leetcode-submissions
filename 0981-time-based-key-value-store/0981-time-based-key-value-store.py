import bisect

class TimeMap:

    ""

    def __init__(self):
        self.time_map = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        # timestamps = [t for t, _ in self.time_map[key]]
        idx = bisect.bisect_right(self.time_map[key], timestamp, key=lambda x: x[0]) -1

        if idx<0:
            return ""

        return self.time_map[key][idx][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)