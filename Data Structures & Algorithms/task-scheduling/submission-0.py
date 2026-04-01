class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxheap= [-s for s in count.values()]
        heapq.heapify(maxheap)

        time=0
        q=deque()

        while q or maxheap:
            time+=1
            if maxheap:
                count=1+heapq.heappop(maxheap)
                if count:
                    q.append([count,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxheap,q.popleft()[0])

        return time