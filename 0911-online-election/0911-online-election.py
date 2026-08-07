class TopVotedCandidate:
    '''
    Pattern - Preprocessing + Binary Search

    Idea:
    1. Process votes once.
    2. Store the leader after every vote.
    3. For each query:
    - Find the last vote whose time <= t (Upper Bound - 1).
    - Return the stored leader.

    Initialization:
    TC - O(N)
    SC - O(N)

    Query:
    TC - O(log N)
    SC - O(1)
    '''

    def __init__(self, persons: List[int], times: List[int]):
        self.leader = []
        self.times = times
        self.vote_cnt = defaultdict(int)
        self.cur_leader = None

        for person in persons:
            self.vote_cnt[person] += 1

            if self.leader == None:
                self.leader.append(person)
                self.cur_leader = person
            elif self.vote_cnt[person] < self.vote_cnt[self.cur_leader]:
                self.leader.append(self.cur_leader)
            else:
                self.leader.append(person)
                self.cur_leader = person
            

    def q(self, t: int) -> int:
        r = bisect_right(self.times, t)-1
        return self.leader[r]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)