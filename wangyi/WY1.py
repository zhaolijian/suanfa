# 小v今年有n门课，每门都有考试，为了拿到奖学金，小v必须让自己的平均成绩至少为avg。
# 每门课由平时成绩和考试成绩组成，满分为r。现在他知道每门课的平时成绩为ai ,
# 若想让这门课的考试成绩多拿一分的话，小v要花bi 的时间复习，不复习的话当然就是0分。
# 同时我们显然可以发现复习得再多也不会拿到超过满分的分数。为了拿到奖学金，小v至少要花多少时间复习。
class Solution:
    def func(self, n, r, avg, array):
        # 总成绩至少值
        sum_number = avg * n
        # 平时成绩总和
        sum_common = 0
        for i in range(n):
            sum_common += array[i][0]
        # 差值
        diff = sum_number - sum_common
        # 注意平时成绩已经满足的情况
        if diff <= 0:
            return 0
        res = 0
        array.sort(key=lambda x: x[1])
        for i in range(n):
            temp = r - array[i][0]
            if temp >= diff:
                res += diff * array[i][1]
                return res
            else:
                diff -= temp
                res += temp * array[i][1]


if __name__ == '__main__':
    while True:
        try:
            # 课程数、满分、平均成绩至少多少
            n, r, avg = map(int, input().split())
            array = []
            for i in range(n):
                array.append(list(map(int, input().split())))
            s = Solution()
            print(s.func(n, r, avg, array))
        except:
            break
