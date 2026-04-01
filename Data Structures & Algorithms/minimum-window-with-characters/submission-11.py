class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tcount = {}
        for ch in t:
            tcount[ch] = 1 + tcount.get(ch, 0)

        scount = {}
        l = 0
        res = float("inf")
        ans = [-1, -1]

        for r in range(len(s)):
            scount[s[r]] = 1 + scount.get(s[r], 0)

            # shrink as long as window is valid
            while True:
                valid = True
                for c in tcount:
                    if scount.get(c, 0) < tcount[c]:
                        valid = False
                        break

                if not valid:
                    break

                # window is valid, try update answer
                if (r - l + 1) < res:
                    res = (r - l + 1)
                    ans = [l, r]

                # ALWAYS shrink one step
                scount[s[l]] -= 1
                l += 1

        l, r = ans
        return "" if res == float("inf") else s[l:r+1]