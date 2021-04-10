# 给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。
# 注意：1 ≤ k ≤ n ≤ 109。

# 字典序
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # 前缀为prefix,上限为n的子节点个数
        def getCount(prefix, n):
            cur, next, count = prefix, prefix + 1, 0
            while cur <= n:
                count += min(next, n + 1) - cur
                cur *= 10
                next *= 10
            return count

        prefix, index = 1, 1
        while index < k:
            temp = getCount(prefix, n)
            if index + temp > k:
                prefix *= 10
                index += 1
            else:
                prefix += 1
                index += temp
        return prefix