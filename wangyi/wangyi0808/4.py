from collections import defaultdict
class Solution:
    def func(self, n, m, array):
        def find(number):
            if
        # d中存储该教授所有信赖的人
        res = 0
        d = defaultdict(set)
        for i in range(m):
            d[array[i][0]].add(array[i][1])

        def dfs()


if __name__ == '__main__':
    while True:
        try:
            s = Solution()
            # 教授人数、认可关系数
            n, m = map(int, input().split())
            array = []
            for i in range(m):
                array.append(list(map(int, input().split())))
            print(s.func(n, m, array))
        except:
            break