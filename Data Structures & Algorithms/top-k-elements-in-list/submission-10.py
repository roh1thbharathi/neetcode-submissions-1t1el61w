class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        mp={}
        for i in nums:
            mp[i]=1+mp.get(i,0)
        
        freq=[[]for i in range(len(nums)+1)]

        for n ,c in mp.items():
            freq[c].append(n)
        
        for i in range(len(freq)-1 ,0,-1):
            for j in freq[i]:
                res.append(j)
            if len(res)>=k:
                return res


