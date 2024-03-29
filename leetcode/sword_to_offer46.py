# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
# 一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。


# 方法1 dfs
class Solution:
    def translateNum(self, num: int) -> int:
        res = 0
        def dfs(rest):
            nonlocal res
            if rest == "":
                res += 1
                return
            dfs(rest[1:])
            if len(rest) >= 2 and "10" <= rest[:2] <= "25":
                dfs(rest[2:])

        num = str(num)
        dfs(num)
        return res


# 方法2 dp
class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        length = len(num)
        dp = [1 for i in range(length + 1)]
        for i in range(2, length + 1):
            if "10" <= num[i - 2: i] <= "25":
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[-1]