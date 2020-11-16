class Solution:
    def findRightInterval(self, intervals):
        sorted_start = [(interval[0], index) for index, interval in enumerate(intervals)]
        sorted_start.sort()
        res = []
        for interval in intervals:
            target = interval[1]
            l = 0
            r = len(intervals)
            while l < r:
                mid = (l + r) // 2
                if sorted_start[mid][0] < target:
                    l = mid + 1
                else:
                    r = mid
            if l == len(intervals):
                res.append(-1)
            else:
                res.append(sorted_start[l][1])
        return res


if __name__ == '__main__':
    s = Solution()
    result = s.findRightInterval([[3,4], [2,3], [1,2]])
    print(result)
