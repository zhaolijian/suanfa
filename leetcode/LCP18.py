# 小扣在秋日市集选择了一家早餐摊位，一维整型数组 staple 中记录了每种主食的价格，一维整型数组 drinks 中记录了每种饮料的价格。
# 小扣的计划选择一份主食和一款饮料，且花费不超过 x 元。请返回小扣共有多少种购买方案。
# 注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1


# 方法1 双指针
class Solution:
    def breakfastNumber(self, staple, drinks, x: int) -> int:
        staple.sort()
        drinks.sort()
        i = 0
        j = len(drinks) - 1
        res = 0
        while i < len(staple) and j >= 0:
            if staple[i] + drinks[j] > x:
                j -= 1
            else:
                res += j + 1
                i += 1
        return res % 1000000007


# 方法2 二分查找
from bisect import bisect_right
class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        staple.sort()
        drinks.sort()
        len_s, len_d = len(staple), len(drinks)
        res = 0
        if len_s > len_d:
            len_s, len_d = len_d, len_s
            staple, drinks = drinks, staple
        for i in range(len_s):
            target = x - staple[i]
            if target <= 0:
                break
            index = bisect_right(drinks, target)
            if index >= len_d:
                res += len_d
            elif drinks[index] == target:
                res += index + 1
            else:
                res += index
        return res % 1000000007