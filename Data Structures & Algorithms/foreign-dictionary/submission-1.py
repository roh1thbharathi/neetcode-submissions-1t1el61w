class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj={c:set()for w in words for c in w}

        for i in range(len(words)-1):
            w1 , w2 = words[i] , words[i+1]
            minlen=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minlen]==w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        res=[]
        visited=set()
        visiting=set()

        def dfs(c):
            if c in visiting:
                return True
            if c in visited:
                return False

            visiting.add(c)
            for nei in adj[c]:
                if dfs(nei):
                    return ""
            visiting.remove(c)
            visited.add(c)
            res.append(c)
            return False

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)