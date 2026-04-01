class Twitter:

    def __init__(self):
        self.count=0
        self.followmap=defaultdict(set)
        self.tweetmap=defaultdict(list)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count,tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        minheap=[]
        self.followmap[userId].add(userId)
        for followee in self.followmap[userId]:
            if followee in self.tweetmap:
                index=len(self.tweetmap[followee])-1
                count , tweetid = self.tweetmap[followee][index]
                heapq.heappush(minheap, [count, tweetid, followee, index - 1])

        while minheap and len(res)<10:
            count , tweetid , followee ,index = heapq.heappop(minheap)
            res.append(tweetid)
            if index>=0:
                count , tweetid = self.tweetmap[followee][index]
                heapq.heappush(minheap, [count, tweetid, followee, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
        
