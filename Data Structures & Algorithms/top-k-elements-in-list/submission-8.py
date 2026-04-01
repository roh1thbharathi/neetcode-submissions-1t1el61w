class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       freq={}
       for i in nums:
        freq[i]=1+freq.get(i,0)
       temp=sorted(freq.items(),reverse=True,key=lambda item:item[1])
       return [item[0] for item in temp[:k]]
       
    