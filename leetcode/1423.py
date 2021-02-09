# 几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。
# 每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。
# 你的点数就是你拿到手中的所有卡牌的点数之和。
# 给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。

# 一共k个元素，左边i个右边k-i个，遍历即可
class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        res = sum(cardPoints[-k:])
        cur = res
        for i in range(k):
            cur += cardPoints[i]
            cur -= cardPoints[-(k - i)]
            if cur > res:
                res = cur
        return res