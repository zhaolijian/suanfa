class Solution:
    # 怪物数、每个金币购买的血量、怪物花费血量和获得金币数组
    def solu(self, n, m, array):
        init = [0 for i in range(n)]
        init[0] = array[0][1] - array[0][0] / 2
        for i in range(1, n):
            init[i] = max(init[i - 1] + array[i][1] - array[i][0] / 2, array[i][1] - array[i][0] / 2)
        max_val = max(init)
        if max_val <= 0:
            return 0
        elif max_val % 1 == 0:
            return int(max_val)
        else:
            return int(max_val) + 1


if __name__ == '__main__':
    l = list(map(int, input().split()))
    n, m = l[0], l[1]
    array = []
    for i in range(n):
        # 怪物花费的血量、获得的金币数
        l = list(map(int, input().split()))
        array.append(l)
    s = Solution()
    print(s.solu(n, m, array))
