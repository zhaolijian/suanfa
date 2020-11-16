class Solution:
    # 怪物数、每个金币购买的血量、怪物花费血量和获得金币数组
    def solu(self, a, b, c):
        if pow(a, 2) - 2 * a * b * c <= 0:
            return 0
        else:
            y1 = (a - pow(pow(a, 2) - 2 * a * b * c, 0.5)) / b
            y2 = (a + pow(pow(a, 2) - 2 * a * b * c, 0.5)) / b
            res2 = pow(y2, 2) / (2 * b) - c * y2 / b - pow(y2, 3) / (6 * a)
            res1 = pow(y1, 2) / (2 * b) - c * y1 / b - pow(y1, 3) / (6 * a)
            return res2 - res1 if res2 - res1 > 0 else 0


if __name__ == '__main__':
    for _ in range(int(input())):
        s = Solution()
        l = list(map(int, input().split()))
        a, b, c = l[0], l[1], l[2]
        print(s.solu(a, b, c))

