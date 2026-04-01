class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count={}
        for task in tasks:
            count[task]=count.get(task,0)+1
        heap=[-c for c in count.values()]
        heapq.heapify(heap)
        q=deque()
        time=0
        while heap or q:
            time+=1
            if heap:
                count=1+heapq.heappop(heap)
                if count:
                    q.append([count,time+n])
            if q and q[0][1]==time:
                heapq.heappush(heap,q.popleft()[0])
        return time