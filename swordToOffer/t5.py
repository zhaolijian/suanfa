class Solution:
    def solu(self, array):
        # 所有的圈子
        res = []
        for i in range(len(array)):
            m, n = array[i][0], array[i][1]
            if not res:
                temp = set()
                temp.add(m)
                temp.add(n)
                res.append(temp)
                continue
            init = []
            for j in range(len(res)):
                if m in res[j] or n in res[j]:
                    res[j].add(m)
                    res[j].add(n)
                    init.append(j)
            if not init:
                temp = set()
                temp.add(m)
                temp.add(n)
                res.append(temp)
            if len(init) > 1:
                for t in range(1, len(init)):
                    res[init[0]] = res[init[0]].union(res[init[t]])
                    res.pop(init[t])
        number = []
        for k in range(len(res)):
            number.append(len(res[k]))
        return max(number) if number else 0


if __name__ == '__main__':
    s = Solution()
    for _ in range(int(input())):
        n = int(input())
        array = []
        for i in range(n):
            l = list(map(int, input().split()))
            array.append(l)
        print(s.solu(array))
