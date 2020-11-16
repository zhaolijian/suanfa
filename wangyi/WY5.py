# 题目描述
# 在N*M的草地上,提莫种了K个蘑菇,蘑菇爆炸的威力极大,兰博不想贸然去闯,而且蘑菇是隐形的.
# 只有一种叫做扫描透镜的物品可以扫描出隐形的蘑菇,于是他回了一趟战争学院,买了2个扫描透镜,
# 一个扫描透镜可以扫描出(3*3)方格中所有的蘑菇,然后兰博就可以清理掉一些隐形的蘑菇. 问:兰博最多可以清理多少个蘑菇?
# 注意：每个方格被扫描一次只能清除掉一个蘑菇。


# 方法1 两个一块找
class Solution:
    def func(self, N, M, init):
        def find(x, y):
            if init[x][y] > 0:
                return 1
            return 0

        def find_sum(x, y):
            return find(x - 1, y - 1) + find(x - 1, y) + find(x - 1, y + 1) + \
                   find(x, y - 1) + find(x, y) + find(x, y + 1) + \
                   find(x + 1, y - 1) + find(x + 1, y) + find(x + 1, y + 1)

        res = 0
        axis = init[:]
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                val1 = find_sum(i, j)
                for p in range(i - 1, i + 2):
                    for q in range(j - 1, j + 2):
                        axis[p][q] -= 1
                for m in range(1, N + 1):
                    for n in range(1, M + 1):
                        val2 = find_sum(m, n)
                        res = max(res, val1 + val2)
                for p in range(i - 1, i + 2):
                    for q in range(j - 1, j + 2):
                        axis[p][q] += 1
        return res


if __name__ == '__main__':
    while True:
        try:
            N, M, K = map(int, input().split())
            init = [[0 for i in range(M + 2)] for j in range(N + 2)]
            for i in range(K):
                x, y = map(int, input().split())
                init[x][y] += 1
            s = Solution()
            print(s.func(N, M, init))
        except:
            break


# 方法2 贪心，这个方法可以ac，但是实际是错的，比如如下测试用例
# 3 7 13
# 1 1
# 1 3
# 1 5
# 1 7
# 2 1
# 2 3
# 2 4
# 2 5
# 2 7
# 3 1
# 3 3
# 3 5
# 3 7
# class Solution:
#     def func(self, N, M, init):
#         def find(x, y):
#             if init[x][y] > 0:
#                 return 1
#             return 0
#
#         res = 0
#         x, y = 0, 0
#         for i in range(1, N + 1):
#             for j in range(1, M + 1):
#                 val = find(i - 1, j - 1) + find(i - 1, j) + find(i - 1, j + 1) + \
#                       find(i, j - 1) + find(i, j) + find(i,j + 1) + \
#                       find(i + 1, j - 1) + find(i + 1, j) + find(i + 1, j + 1)
#                 if val > res:
#                     res = val
#                     x, y = i, j
#         return res, x, y
#
#
# if __name__ == '__main__':
#     while True:
#         try:
#             N, M, K = map(int, input().split())
#             init = [[0 for i in range(M + 2)] for j in range(N + 2)]
#             for i in range(K):
#                 x, y = map(int, input().split())
#                 init[x][y] += 1
#             s = Solution()
#             one_search, x, y = s.func(N, M, init)
#             for i in range(x - 1, x + 2):
#                 for j in range(y - 1, y + 2):
#                     if init[i][j] > 0:
#                         init[i][j] -= 1
#             two_search, x, y = s.func(N, M, init)
#             print(one_search + two_search)
#         except:
#             break


