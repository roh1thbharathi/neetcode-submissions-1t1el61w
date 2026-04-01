class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]        

    def addNum(self, num: int) -> None:
        #push values
        if self.large and num> self.large[0]:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,-num)

        #balance lengths
        if len(self.large) > len(self.small)+1:
            val=heapq.heappop(self.large)
            heapq.heappush(self.small,-val)
        if len(self.small) > len(self.large)+1:
            val=-heapq.heappop(self.small)
            heapq.heappush(self.large,val)
    
    def findMedian(self) -> float:
        #odd cases
        if len(self.large) > len(self.small):
            return self.large[0]
        if len(self.small) > len(self.large):
            return -self.small[0]
        #even
        return ( -self.small[0]+self.large[0])/2