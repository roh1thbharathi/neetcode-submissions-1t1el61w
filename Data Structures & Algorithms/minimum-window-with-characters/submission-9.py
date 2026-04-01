class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""

        count={}
        window={}
        res=[-1,-1]
        reslen=float("infinity")
        l=0

        for i in range(len(t)):
            count[t[i]]=1+count.get(t[i],0)

        i=0
        for i in range(len(s)):
            window[s[i]]=1+window.get(s[i],0)

            while all(window.get(c,0)>=count[c] for c in count):
                if(i-l+1)<=reslen:
                    res=[l,i]
                    reslen=(i-l+1)
                window[s[l]]-=1
                l+=1

        l,i=res
        if reslen<float("infinity"):
            return s[l:i+1]
        else:
            return ""
