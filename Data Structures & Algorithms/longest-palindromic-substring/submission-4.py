class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for i in range(n)]

        res = ""
        resLen = 0

        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True

                    if r - l + 1 > resLen:
                        res = s[l:r + 1]
                        resLen = r - l + 1

        return res


# Note:
# 1. r-l<=2 check in dp sol

# 2. there is a two pointer sol as well expanding from centre know both