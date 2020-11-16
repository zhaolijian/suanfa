class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = intervals[i][1] if intervals[i][1] > res[-1][1] else res[-1][1]
        return res


if __name__ == '__main__':
    s = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(s.merge(intervals))