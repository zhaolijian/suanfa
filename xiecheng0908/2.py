# 题目描述：
# 已知矩形的行和列，请按如下规律输出斜对角矩形。
# 例1：
# 输入：2 2
# 输出：[[1,3],[2,4]]
#
# 例2：
# 输入：1 2
# 输出：[[1, 2]]
#
# 输入：4 3
#
# [[1, 3, 6], [2, 5, 9], [4, 8, 11], [7, 10, 12]]
#
#
#
# 输入描述
# 矩阵的行和列大小
#
# 输出描述
# 按规律输出的矩阵

if __name__ == '__main__':
    while True:
        try:
            h, w = map(int, input().split())
            # 行和列相加为0。。。h + w - 2
            init = [[0 for i in range(w)] for j in range(h)]
            number = 1
            for k in range(h + w - 1):
                for i in range(k, -1, -1):
                    if i < h and k - i < w:
                        init[i][k - i] = number
                        number += 1
            print(init)

        except:
            break