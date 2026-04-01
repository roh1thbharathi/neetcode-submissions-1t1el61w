class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countt = {}
        window = {}

        for i in range(len(t)):
            countt[t[i]] = 1 + countt.get(t[i], 0)

        res = [-1, -1]
        resLen = float("infinity")
        l = 0

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            # Check if window meets requirements by comparing dictionaries
            while all(window.get(c, 0) >= countt[c] for c in countt):
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                window[s[l]] -= 1
                l += 1

        l, r = res
        if resLen != float("infinity"):
            return s[l:r+1]
        else:
            return ""
