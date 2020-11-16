# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。


# dfs + 剪枝
class Solution:
    def combine(self, n: int, k: int):
        result = []

        def recall(start, subset):
            # 剪枝
            if len(subset) == k:
                result.append(subset)
                return
            for i in range(start, n+1):
                if k - len(subset) > n - i + 1:
                    break
                recall(i+1, subset + [i])
        recall(1, [])
        return result
