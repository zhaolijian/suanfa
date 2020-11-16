# 景点8点开门，买票人数为n，array为每个人的买票时间，array1为相邻两个人一起的买票时间，问怎么安排能尽早关门，输出关门时间
# 12点多算am，出题人脑子瓦特了？？？
class Solution:
    def func(self, n, array, array2):
        if not array2:
            return array[0]
        dp =[0 for i in range(n)]
        dp[0] = array[0]
        dp[1] = min(array[0] + array[1], array2[0])
        for i in range(2, n):
            dp[i] = min(dp[i - 1] + array[i], dp[i - 2] + array2[i - 1], dp[i - 2] + array[i - 1] + array[i])
        return dp[-1]


if __name__ == '__main__':
    T = int(input())
    solution = Solution()
    for i in range(T):
        # 买票人数
        n = int(input())
        array = list(map(int, input().split()))
        array2 = input()
        array2 = [] if not array2 else list(map(int, array2.split()))
        result = solution.func(n, array, array2)
        h, m, s = 8, 0, 0
        if result >= 3600:
            h += result // 3600
            result %= 3600
        if result >= 60:
            m += result // 60
            result %= 60
        if h >= 24:
            h %= 24
        s += result
        # 上午是true,下午是false
        flag = True
        if h > 12 or (h == 12 and (m > 0 or s > 0)):
            flag = False
        if h >= 13:
            h -= 12
        s_h, s_m, s_s = str(h), str(m), str(s)
        len_h, len_m, len_s = len(s_h), len(s_m), len(s_s)
        if len_h == 1:
            s_h = '0' + s_h
        if len_m == 1:
            s_m = '0' + s_m
        if len_s == 1:
            s_s = '0' + s_s
        if flag:
            print(s_h + ':' + s_m + ':' + s_s + ' ' + 'am')
        else:
            print(s_h + ':' + s_m + ':' + s_s + ' ' + 'pm')