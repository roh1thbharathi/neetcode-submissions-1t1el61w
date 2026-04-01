class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[float("inf")]*n
        prices[src]=0

        for i in range(k+1):
            temp=prices.copy()
            for s,d,c in flights:
                if temp[s]==float("inf"):
                    continue
                if prices[s]+c<temp[d]:
                    temp[d]=prices[s]+c
            prices=temp

        if prices[dst]==float("inf"):
            return -1
        else:
            return prices[dst]

        