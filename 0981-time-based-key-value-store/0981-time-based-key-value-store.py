class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        
        i = len(self.time_map[key])-1
        while i>=0 and self.time_map[key][i][0]>timestamp:
            i-=1
        
        if i<0:
            return ""

        return self.time_map[key][i][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)