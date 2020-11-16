# coding=utf-8
# 有一楼梯共m级，刚开始时你在第一级，若每次只能跨上一级或者二级，要走上m级，共有多少走法？注：规定从一级到一级有0种走法。
# 给定一个正整数int n，请返回一个数，代表上楼的方式数。保证n小于等于100。为了防止溢出，请返回结果Mod 1000000007的值。
# 测试样例：
# 3
# 返回：2


class GoUpstairs:
    def countWays(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 1
        dp = [1, 1]
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[-1] % 1000000007