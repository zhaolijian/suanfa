# 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，
# 这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
# 请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
# 说明:
# 不允许旋转信封。


# 单调递增子序列的变形
# 主要在于sort操作，宽度递增，若宽度相同，高度递减
# 原因在于，若宽度单调递增，求高度最长连续子序列，那么若宽度相等时，可能会出现多个相同宽度对应的高度出现在最长连续子序列中
# 若相同宽度的条件下，高度递减，则相同宽度只可能有一个高度出现在LIS（最长上升子序列）中
from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        if not envelopes:
            return 0
        length = len(envelopes)
        # 存储高度的递增序列
        res = []
        for i in range(length):
            if not res or envelopes[i][1] > res[-1]:
                res.append(envelopes[i][1])
            else:
                index = bisect_left(res, envelopes[i][1])
                res[index] = envelopes[i][1]
        return len(res)


if __name__ == '__main__':
    s = Solution()
    envelopes = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
    print(s.maxEnvelopes(envelopes))
