class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        dp = [0] * n

        for i in range(n):
            dp[i] = 1
            for j in range(i):
                if intervals[j][1] <= intervals[i][0]:
                    dp[i] = max(dp[i], 1 + dp[j])

        max_non_overlapping = max(dp)
        return n - max_non_overlapping



# Backtracking / Memo:

# At index i, you do:
# take OR skip

# So you explore:
# include current interval
# exclude current interval

# 👉 This guarantees:
# you will eventually consider all possible subsets, regardless of order
# So sorting is optional (just helps performance/pruning).





# Bottom-up DP

# You changed the perspective:
# dp[i] = best solution ending at i
# And you compute it using:

# for j in range(i):

# 👉 This means:
# “I will ONLY look at intervals before me”

# So DP assumes:
# all useful previous intervals must already be before i
# Why sorting becomes necessary

# Without sorting:
# 👉 Some valid previous intervals may appear after i in the array
# But DP will never look forward, only backward.
# So you miss valid chains.