class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_map = {}
        self.cuisine_map = defaultdict(list)

        for f,c,r in zip(foods, cuisines, ratings):
            self.food_map[f] = (r,c)
            heapq.heappush(self.cuisine_map[c], (-r, f))
        

    def changeRating(self, food: str, newRating: int) -> None:
        r,c = self.food_map[food]
        self.food_map[food] = (newRating, c)
        heapq.heappush(self.cuisine_map[c],(-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        max_heap = self.cuisine_map[cuisine]

        while max_heap:
            r, f = max_heap[0]

            if self.food_map[f][0] == -r:
                return f
            
            heapq.heappop(self.cuisine_map[cuisine])


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)