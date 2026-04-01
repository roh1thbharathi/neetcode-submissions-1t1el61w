class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1=len(s1)
        len2=len(s2)
        if len1>len2:
            return False
        freq1=[0]*26
        freq2=[0]*26
        for i in range (len1):
            freq1[ord(s1[i])-ord('a')]+=1
            freq2[ord(s2[i])-ord('a')]+=1
        if freq1==freq2:
            return True
        for i in range (len1,len2):
            freq2[ord(s2[i])-ord('a')]+=1
            freq2[ord(s2[i-len1])-ord('a')]-=1
            if freq1==freq2:
                return True
        return False