class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        intervals.sort(key=lambda x:x[0])
        output=[]
        output.append(intervals[0])

        for start,end in intervals[1:]:
            lastend=output[-1][1]

            if start<=lastend:
                output[-1][1]=max(lastend,end)

            else:
                output.append([start,end])

        return output