class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp={}
        temp=[]
        res=[]

        for i in nums:
            mp[i]=mp.get(i,0)+1

        for n,c in mp.items():
            temp.append([n,c])

        temp.sort(key=lambda x: x[1], reverse=True)

        for c,n in temp:
            if len(res)<k:
                res.append(c)

        return res