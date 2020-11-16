# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
# 说明：
# 所有数字都是正整数。
# 解集不能包含重复的组合。 

class Solution:
    def combinationSum3(self, k: int, n: int):
        res = []

        # 当前数、当前集合、还差多少
        def func(cur, s, rest):
            if len(s) == k and rest == 0:
                res.append(sorted(list(s)))
                return
            if rest < 0:
                return
            if rest == 0 and len(s) < k:
                return
            for i in range(cur, 10):
                if (i + 9) * (9 - i + 1) / 2 < rest:
                    return
                s.add(i)
                func(i + 1, s, rest - i)
                s.remove(i)
        if k > 9 or n > ((9 - k + 1) + 9) * k / 2 or n < (1 + k) * k / 2:
            return []
        func(1, set(), n)
        return res


if __name__ == '__main__':
    s = Solution()
    k = 3
    n = 7
    print(s.combinationSum3(k, n))