# 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
# 你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

# 二维dp
class Solution:
    def dicesProbability(self, n: int):
        # 纵坐标表示骰子数,横坐标表示n个骰子的值,对应的二维值为n个骰子扔出该值的次数
        dp = [[0 for i in range(6 * n)] for j in range(n)]
        # 一个骰子可能出现的值是1-6,次数为1
        for i in range(6):
            dp[0][i] = 1
        for i in range(1, n):
            for j in range((i + 1) * 6):
                for k in range(1, 7):
                    if j < k:
                        break
                    dp[i][j] += dp[i - 1][j - k]
        # 所有可能出现的次数
        sum_val = sum(dp[-1])
        res = []
        for ele in dp[-1]:
            if ele != 0:
                res.append(ele / sum_val)
        return res


# 一维dp
class Solution:
    def dicesProbability(self, n: int):
        dp = [0 for i in range(6 * n)]
        # 一个骰子的初始化
        for i in range(6):
            dp[i] = 1
        for i in range(1, n):
            for j in range((i + 1) * 6 - 1, -1, -1):
                # 不要忘了该步
                dp[j] = 0
                for k in range(1, 7):
                    if j < k:
                        break
                    dp[j] += dp[j - k]
        sum_val = sum(dp)
        return [dp[i] / sum_val for i in range(n - 1, 6 * n)]