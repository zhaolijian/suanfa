class Solution:
    def waysToChange(self, n: int) -> int:
        mod = 10**9 + 7
        coins = [1, 5, 10, 25]
        f = [1] + [0] * n
        # 先用小的，再用大的，这样可以防止出现15 和 51的情况（coins数组倒过来也行，先用大的再用小的）
        for coin in coins:
            for i in range(coin, n + 1):
                f[i] += f[i - coin]
        return f[n] % mod


if __name__ == '__main__':
    s = Solution()
    n = 61
    print(s.waysToChange(n))