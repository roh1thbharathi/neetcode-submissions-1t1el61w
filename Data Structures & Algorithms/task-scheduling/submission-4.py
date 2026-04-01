class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp={}
        for i in range(len(tasks)):
            mp[tasks[i]]=mp.get(tasks[i],0)+1

        heap=[-c for c in mp.values()]
        heapq.heapify(heap)
        time=0
        q=deque()

        while heap or q:
            time+=1
            if heap:
                count=1+heapq.heappop(heap)
                if count:
                    q.append([count,time+n])
            if q and q[0][1]==time:
                heapq.heappush(heap,q.popleft()[0])

        return time