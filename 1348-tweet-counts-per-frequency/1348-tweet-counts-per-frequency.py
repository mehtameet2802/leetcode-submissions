class TweetCounts:

    def __init__(self):
        self.tweet_dict = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweet_dict[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        chunk = {
            "minute": 60,
            "hour": 3600,
            "day": 86400
        }[freq]

        n = (endTime - startTime) // chunk + 1

        ans = [0]*n

        tweet_time = self.tweet_dict[tweetName]

        for t in tweet_time:
            if t < startTime or t > endTime:
                continue

            idx = (t-startTime) // chunk

            ans[idx] += 1
        
        return ans


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)