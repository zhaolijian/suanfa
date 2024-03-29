# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        return (self.numWays(n - 1) + self.numWays(n - 2)) % 1000000007



# 方法2
class Solution:
    @lru_cache(None)
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        init = [1, 1]
        for i in range(2, n + 1):
            init.append((init[-1] + init[-2]) % 1000000007)
        return init[-1]