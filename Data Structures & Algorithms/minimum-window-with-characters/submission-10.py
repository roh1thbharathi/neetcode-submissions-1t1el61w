class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""

        tcount={}
        for i in range(len(t)):
            tcount[t[i]]=1+tcount.get(t[i],0)

        scount={}
        l=0
        res=float("infinity")
        ans=[-1,-1]

        for i in range(len(s)):
            scount[s[i]]=1+scount.get(s[i],0)

            while all(scount.get(c,0)>=tcount[c] for c in tcount):
                if (i-l+1)<res:
                    res=(i-l+1)
                    ans=[l,i]
                scount[s[l]]-=1
                l+=1

        l,r=ans
        if res<float("infinity"):
            return s[l:r+1]
        else:
            return ""