# 今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。
# 在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。
# 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。
# 书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。
# 请你返回这一天营业下来，最多有多少客户能够感到满意的数量。


# 双指针
class Solution:
    def maxSatisfied(self, customers, grumpy, X: int) -> int:
        length = len(customers)
        # 本来就不生气的时间总顾客数
        init = sum(customers[i] for i in range(length) if grumpy[i] == 0)
        # res: 连续X分钟原本生气使用技巧后变的不生气时间的最大总顾客数
        res, cur, left, right = 0, 0, 0, 0
        while right < length:
            if grumpy[right] == 1:
                cur += customers[right]
                res = max(res, cur)
            if right - left + 1 >= X:
                if grumpy[left] == 1:
                    cur -= customers[left]
                left += 1
            right += 1
        return init + res


# 和上面思想基本一样，不需判断grumpy[right]是否为1，只需要customers[i]、grumpy[i]乘积即可，如果grumpy[right]为1，则结果为customers[i]，否则结果为0
class Solution:
    def maxSatisfied(self, customers, grumpy, X: int) -> int:
        length = len(customers)
        # 本来就不生气的时间总顾客数
        init = sum(customers[i] for i in range(length) if grumpy[i] == 0)
        # res: 连续X分钟原本生气使用技巧后变的不生气时间的最大总顾客数
        res = cur = sum(customers[i] * grumpy[i] for i in range(X))
        for right in range(X, length):
            cur += customers[right] * grumpy[right] - customers[right - X] * grumpy[right - X]
            res = max(res, cur)
        return init + res
