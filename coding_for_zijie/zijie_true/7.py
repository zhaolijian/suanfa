# 题目描述
# 【编码题】字符串S由小写字母构成，长度为n。定义一种操作，每次都可以挑选字符串中任意的两个相邻字母进行交换。
# 询问在至多交换m次之后，字符串中最多有多少个连续的位置上的字母相同？
# 输入描述:
# 第一行为一个字符串S与一个非负整数m。(1 <= |S| <= 1000, 1 <= m <= 1000000)
# 输出描述:
# 一个非负整数，表示操作之后，连续最长的相同字母数量。
from collections import defaultdict
if __name__ == '__main__':
    l = list(input().split())
    S = l[0]
    m = int(l[-1])
    res = 1
    # 存放每个字母对应位置
    chars = defaultdict(list)
    for i, ele in enumerate(S):
        chars[ele].append(i)
    for key in chars.keys():
        l = chars[key]
        length = len(l)
        dp = [[0 for i in range(length)] for j in range(length)]
        for i in range(1, length):
            dp[i - 1][i] = l[i] - l[i - 1] - 1
        for width in range(2, length):
            for start in range(length - width):
                i, j = start, start + width
                dp[i][j] = dp[i + 1][j - 1] + l[j] - l[i] - (j - i)
        for i in range(length):
            for j in range(i + 1, length):
                if dp[i][j] <= m:
                    res = max(res, j - i + 1)
    print(res)