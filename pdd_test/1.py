class Solution:
    # 盒子数量，每个盒子中的球数
    def solu(self, n, l):
        max_value = max(l) + 1
        res = 0
        for i in range(len(l) - 1):
            if l[i] == l[i + 1]:
                res += max_value - l[i]
        for j in range(len(l)):

        return res


if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
    s = Solution()
    print(s.solu(n, l))
