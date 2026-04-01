class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1= len(s1)
        len2= len(s2)

        if len1 > len2:
            return False

        freq1={}
        freq2={}


        for i in range(len1):
            freq1[s1[i]]=1+freq1.get(s1[i],0)
            freq2[s2[i]]=1+freq2.get(s2[i],0)

        if freq1==freq2:
            return True

        for i in range(len1, len2):
            freq2[s2[i]]=1+freq2.get(s2[i],0)
            lastletter=s2[i-len1]
            freq2[lastletter]-=1
            if freq2[lastletter]==0:
                del freq2[lastletter]
            if freq1==freq2:
                return True

        return False