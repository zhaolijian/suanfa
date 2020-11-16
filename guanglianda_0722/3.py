# 输入第一行包含一个两个正整数n和y，分别表示怪物的数量和技能的范围。（1<=n<=100000）
# 接下来有n行，每行有两个正整数x和hp分别表示一只怪物的位置和血量。(1<=x,hp<=10^9)
# 3 5
# 1 10
# 10 5
# 22 3
#
# 13
class Solution:
    def func(self, n, y, array):
        array.sort(key=lambda x: x[0])
        res = 0
        for i in range(len(array)):
            if array[i][1] > 0:
                res += array[i][1]
                temp = array[i][1]
                for j in range(i, len(array)):
                    if array[j][0] <= array[i][0] + 2 * y:
                        if array[j][1] <= temp:
                            array[j][1] = 0
                        else:
                            array[j][1] -= temp
        return res


if __name__ == '__main__':
    s = Solution()
    array1 = list(map(int, input().strip().split()))
    n, y = array1[0], array1[1]
    array = []
    for i in range(n):
        temp = list(map(int, input().strip().split()))
        array.append(temp)
    print(s.func(n, y, array))