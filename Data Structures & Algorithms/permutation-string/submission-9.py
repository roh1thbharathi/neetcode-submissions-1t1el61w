class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1={}
        freq2={}
        n=len(s1)
        m=len(s2)

        if n > m:          
            return False

        for i in range(n):
            freq1[s1[i]]=freq1.get(s1[i],0)+1
            freq2[s2[i]]=freq2.get(s2[i],0)+1

        if freq1==freq2:
            return True

        for i in range(n,m):
            freq2[s2[i]]=freq2.get(s2[i],0)+1
            leftelement=s2[i-n]
            freq2[leftelement]-=1

            if freq2[leftelement]==0:
                del freq2[leftelement]

            if freq1==freq2:
                return True

        return False