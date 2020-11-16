# 现在有n个物品，每个物品都有一个价值，现在想将这些物品分给两个人，要求这两个人分到的物品价值总和相同(个数可以不同，总价值相同即可)，剩下的物品就要扔掉，现在想知道最少需要扔多少价值的物品才能满足要求分给两个人。
# 输入描述
# 第一行输入一个整数T，代表有T组测试数据
# 对于每一组测试数据，一行输入一个整数n，代表物品的个数
# 接下来n个数，a[i]代表每一个物品的价值
# 1 <= T <= 10
# 1 <= n <= 15
# 1 <= a[i] <= 100000
# 输出描述
# 每一行输出最少需要扔掉多少价值的物品


# 暴力解法
class Solution:
    def func(self, n, array):
        # 当前遍历索引、第一个人拥有的物品价值、第二个人拥有的物品价值、抛弃的物品价值
        def dfs(cur, l, r):
            nonlocal res, sum_number
            if cur == n:
                if l == r:
                    res = min(res, sum_number - 2 * l)
                return
            dfs(cur + 1, l + array[cur], r)
            dfs(cur + 1, l, r + array[cur])
            dfs(cur + 1, l, r)

        sum_number = sum(array)
        res = sum_number
        dfs(0, 0, 0)
        return res


# 暴力2
class Solution:
    def func(self, n, array):
        # 当前遍历索引、第一个人拥有的物品价值、第二个人拥有的物品价值、抛弃的物品价值
        def dfs(cur, l, r, drop):
            nonlocal res
            if cur == n:
                if l == r:
                    res = min(res, drop)
                return
            dfs(cur + 1, l + array[cur], r, drop)
            dfs(cur + 1, l, r + array[cur], drop)
            dfs(cur + 1, l, r, drop + array[cur])

        res = sum(array)
        dfs(0, 0, 0, 0)
        return res


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        array = list(map(int, input().split()))
        s = Solution()
        print(s.func(n, array))