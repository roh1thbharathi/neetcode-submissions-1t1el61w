class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        size=[]
        res=""

        for s in strs:
            size.append(len(s))

        for s in size:
            res+=str(s)
            res+=","

        res+="#"

        for s in strs:
            res+=s

        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        i=0
        size=[]
        res=[]

        while s[i]!="#":
            curr=""
            while s[i]!=",":
                curr+=s[i]
                i+=1
            size.append(int(curr))
            i+=1
        i+=1

        for m in size:
            res.append(s[i:i+m])
            i=i+m

        return res














