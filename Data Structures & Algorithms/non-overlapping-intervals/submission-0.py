class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        memo = {}

        def dfs(i, prev):
            if i == len(intervals):
                return 0

            if (i, prev) in memo:
                return memo[(i, prev)]

            res = dfs(i + 1, prev)

            if prev == -1 or intervals[prev][1] <= intervals[i][0]:
                res = max(res, 1 + dfs(i + 1, i))

            memo[(i, prev)] = res
            return res

        return len(intervals) - dfs(0, -1)