# 给定一个边长数组，使之组成面积最大的平行四边形（矩形是平行四边形中最大的）
import collections
class Solution:
    def func(self, n, array):
        d = collections.Counter(array)
        temp = []
        for key in d.keys():
            if d[key] >= 2:
                temp.append(key)
        temp.sort()
        if not temp:
            return -1
        elif d[temp[-1]] >= 4:
            return temp[-1] * temp[-1]
        elif len(temp) < 2:
            return -1
        return temp[-1] * temp[-2]


if __name__ == '__main__':
    s = Solution()
    n = int(input())
    array = list(map(int, input().strip().split()))
    print(s.func(n, array))